data = []
count = 0 #計數器
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料')
#print(data)
#print(data[0])
#print('----------------------------------')
#print(data[1])
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度是',sum_len/len(data),'字')

new = []
for d in data:
	if len(d) <100:
		new.append(d)
print('一共有',len(new),'筆資料小於100')
print(new[0])
print(new[15])