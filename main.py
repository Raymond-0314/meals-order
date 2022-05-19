#import data--------------------------------------------------------------------------------------
from csv import reader
with open('input.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = reader(csv_file)
    data_list = list(csv_reader)
    print(data_list)


#餐點種類與金額--------------------------------------------------------------------------------------
food = [[0,0], [0,0], [0,0], [0,0], [0,0]]
#星期一
food[0] = ['酥炸排骨', 80]
#星期二
food[1] = ['滷雞腿', 85]
#星期三
food[2] = ['素食', 70]
#星期四
food[3] = ['紅燒獅子頭', 70]
#星期五
food[4] = ['香煎鯖魚', 80]


#list初始--------------------------------------------------------------------------------------
import csv
#ouput list 初始
kshs_output = [['學校A', ' ', '星期一', '星期二', '星期三', '星期四', '星期五'], ['姓名', '班級', food[0][0], food[1][0], food[2][0], food[3][0], food[4][0], '金額']]
kghs_output = [['學校B', ' ', '星期一', '星期二', '星期三', '星期四', '星期五'], ['姓名', '班級', food[0][0], food[1][0], food[2][0], food[3][0], food[4][0], '金額']]
kshs_index = 2
kghs_index = 2
#星期1-5分別的金額
#最後是本週總金額
money_day_kshs = [' ', '本週每日金額', 0, 0, 0, 0, 0, 0]
money_day_kghs = [' ', '本週每日金額', 0, 0, 0, 0, 0, 0]
#星期1-5分別的餐點份數
meals_count_kshs = [' ', '本週每日餐點份數', 0, 0, 0, 0, 0]
meals_count_kghs = [' ', '本週每日餐點份數', 0, 0, 0, 0, 0]


#處理data--------------------------------------------------------------------------------------
#人數
num_of_people = len(data_list)
print(num_of_people)
for i in range(1, num_of_people):
  #有訂餐日期0沒有1有
  order_day = [0, 0, 0, 0, 0]
   
  #星期改數字 用迴圈處理
  if data_list[i][4].find('一') != -1:
    order_day[0] = 1
  if data_list[i][4].find('二') != -1:
    order_day[1] = 1
  if data_list[i][4].find('三') != -1:
    order_day[2] = 1
  if data_list[i][4].find('四') != -1:
    order_day[3] = 1
  if data_list[i][4].find('五') != -1:
    order_day[4] = 1
  if data_list[i][4].find('五') != -1:
    order_day[4] = 1

  #金額
  money = order_day[0]*food[0][1] + order_day[1]*food[1][1] + order_day[2]*food[2][1] + order_day[3]*food[3][1] + order_day[4]*food[4][1]

  #建立outputlist
  person_output = [data_list[i][1], data_list[i][3], order_day[0]*food[0][1], order_day[1]*food[1][1], order_day[2]*food[2][1], order_day[3]*food[3][1], order_day[4]*food[4][1], money]
 
  #find school
  if data_list[i][2]=='雄中':
    kshs_output.insert(kshs_index, person_output)
    kshs_index = kshs_index + 1
    for j in range(5): #day 0-4
      money_day_kshs[j+2] = money_day_kshs[j+2] + order_day[j] * food[j][1]
      meals_count_kshs[j+2] = meals_count_kshs[j+2] + order_day[j]
  else:
    kghs_output.insert(kghs_index, person_output)
    kghs_index = kghs_index + 1
    for j in range(5): #day 0-4
      money_day_kghs[j+2] = money_day_kghs[j+2] + order_day[j] * food[j][1]
      meals_count_kghs[j+2] = meals_count_kghs[j+2] + order_day[j]
#算總金額
money_day_kshs[7] = money_day_kshs[2] + money_day_kshs[3] + money_day_kshs[4] + money_day_kshs[5] + money_day_kshs[6]
money_day_kghs[7] = money_day_kghs[2] + money_day_kghs[3] + money_day_kghs[4] + money_day_kghs[5] + money_day_kghs[6]


#printCSV--------------------------------------------------------------------------------------
with open('schoolA.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)
  # 寫入
  writer.writerows(kshs_output)
  writer.writerow([' '])
  writer.writerow(meals_count_kshs)
  writer.writerow(money_day_kshs)
with open('schoolA.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)
  # 寫入
  writer.writerows(kghs_output)
  writer.writerow([' '])
  writer.writerow(meals_count_kghs)
  writer.writerow(money_day_kghs)