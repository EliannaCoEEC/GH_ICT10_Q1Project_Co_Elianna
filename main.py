# receipt generator
from pyscript import display, document

def receipt_generator(e):
    document.getElementById('result').innerHTML = " " # clear the previous output

    pepperoni = document.getElementById('pepperoni')
    cheese = document.getElementById('cheese')
    trufflegreens = document.getElementById('trufflegreens')
    spinach = document.getElementById('spinach')

    subtotal  = float(pepperoni.value) * pepperoni.checked + float(cheese.value) * cheese.checked + float(trufflegreens.value) * trufflegreens.checked + float(spinach.value) * spinach.checked

    vat = subtotal * 0.12
    total = vat + subtotal

    document.getElementById('result').innerHTML = f'<br><i>Receipt</i><br><span style="font-size:20px">Subtotal: ₱{subtotal}<br>Tax: ₱{vat}<br><b>Total: ₱{total}</b></span>'

def sku_generator(e):
    document.getElementById('result').innerHTML = " " # clear the previous output

    pizza = document.getElementById('pizza')
    chicken = document.getElementById('chicken')
    beverages = document.getElementById('beverages')
    sides = document.getElementById('sides')
    product = document.getElementById('text1').value
    stock = document.getElementById('number1').value

    sku  = 'Pizza' * pizza.selected + 'Chicken' * chicken.selected + 'Beverages' * beverages.selected + 'Sides' * sides.selected

    product1 = product.replace(" ", "")

    document.getElementById('result').innerHTML = f'<br><i>Your generated SKU</i><br><span style="font-size:20px">{sku}{product1}{stock}</b></span>'