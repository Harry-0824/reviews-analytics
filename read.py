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
#print(new[0])
#print(new[15])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有',len(good),'筆資料有good')
# print(good[0])

good = [d for d in data if 'good' in d]
print('一共有',len(good),'筆資料有good')

bad = ['bad' in d for d in data]
print(bad)