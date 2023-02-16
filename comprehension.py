# prices = [100,200,300,400];

# dou_prices = [];
# for price in prices:
#     dou_prices.append(price*2);
# print(dou_prices)

# double_price = [price*2 for price in prices]
# print(double_price);


nums = [1,2,3,4,5,6,7,8,9,10];

# even_nums = [];
# for num in nums:
#     if (num%2)==0:
#         even_nums.append(num);
# print(even_nums);

even_nums=[num for num in nums if(num%2)==0];
print(even_nums);