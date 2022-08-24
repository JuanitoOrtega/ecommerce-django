from django.shortcuts import render, redirect
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, Payment, OrderProduct
import json
from store.models import Product

# Create your views here.
def payments(request):
  body = json.loads(request.body)
  order = Order.objects.get(user=request.user, is_ordered=False, order_number=body['orderID'])

  payment = Payment(
    user = request.user,
    payment_id = body['transID'],
    payment_method = body['payment_method'],
    amount_id = order.order_total,
    status = body['status'],
  )
  payment.save()

  order.payment = payment
  order.is_ordered = True
  order.save()

  # Mover todos los carrito items hacia la tabla order product
  cart_items = CartItem.objects.filter(user=request.user)

  for item in cart_items:
    orderproduct = OrderProduct()
    orderproduct.order_id = order.id
    orderproduct.payment = payment
    orderproduct.user_id = request.user.id
    orderproduct.product_id = item.product_id
    orderproduct.quantity = item.quantity
    orderproduct.product_price = item.product.price
    orderproduct.ordered = True
    orderproduct.save()

    # Agrega variaciones a la orden del producto
    cart_item = CartItem.objects.get(id=item.id)
    product_variation = cart_item.variations.all()
    orderproduct = OrderProduct.objects.get(id=orderproduct.id)
    orderproduct.variation.set(product_variation)
    orderproduct.save()

    # Actualizar stock y carrito de compras
    product = Product.objects.get(id=item.product_id)
    product.stock -= item.quantity
    product.save()

    # Limpiamos el carrito despues de que el cliente ordene la compra
    CartItem.objects.filter(user=request.user).delete()
  
  return render(request, 'orders/payments.html')

def place_order(request, total=0, quantity=0):
  current_user = request.user
  cart_items = CartItem.objects.filter(user=current_user)
  cart_count = cart_items.count()

  if cart_count <= 0:
    return redirect('store')
  
  tax = 0
  total_tax = 0

  for cart_item in cart_items:
    total += (cart_item.product.price * cart_item.quantity)
    quantity += cart_item.quantity

  pre_tax = (2 * total) / 100
  tax = round(pre_tax, 2) # redondeamos a 2 decimaes
  pre_total_tax = total + tax
  total_tax = round(pre_total_tax, 2) # redondeamos a 2 decimaes

  if request.method == 'POST':
    form = OrderForm(request.POST)
    
    if form.is_valid():
      data = Order()
      data.user = current_user
      data.first_name = form.cleaned_data['first_name']
      data.last_name = form.cleaned_data['last_name']
      data.phone = form.cleaned_data['phone']
      data.email = form.cleaned_data['email']
      data.address_line_1 = form.cleaned_data['address_line_1']
      data.address_line_2 = form.cleaned_data['address_line_2']
      data.city = form.cleaned_data['city']
      data.state = form.cleaned_data['state']
      data.country = form.cleaned_data['country']
      data.order_note = form.cleaned_data['order_note']
      data.tax = tax
      data.order_total = total_tax
      data.ip = request.META.get('REMOTE_ADDR')
      data.save()

      yr=int(datetime.date.today().strftime('%Y'))
      mt=int(datetime.date.today().strftime('%m'))
      dt=int(datetime.date.today().strftime('%d'))
      d = datetime.date(yr,mt,dt)
      current_date = d.strftime('%Y%m%d')
      # 20280110
      order_number = current_date + str(data.id)
      data.order_number = order_number
      data.save()

      order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
      context = {
        'order': order,
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'total_tax': total_tax,
      }

      return render(request, 'orders/payments.html', context)
  else:
    return redirect('checkout')
