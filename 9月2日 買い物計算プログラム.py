member = int(input('会員ですか？(1:はい 2:いいえ) 1か2で入力してください'))

price = int (input('商品の値段を入力してください'))
count = int (input('商品の個数を入力してください'))

sum_price = price*count

if member == 1 :
   new_sum_price = int(sum_price * 0.9)
else:
    new_sum_price = sum_price




if sum_price >= 3000:
    send_price = 0

else:
    send_price = 500

total_price = new_sum_price + send_price

print(f'送料は{send_price}円です')
print(f'お支払い金額は{total_price}円です')

