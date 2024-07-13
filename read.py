data = []
count = 0 #計數器
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了,總共有',len(data),'筆資料')

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

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆資料有good')
print(good[0])

good = [d for d in data if 'good' in d]
print('一共有',len(good),'筆資料有good')


# 文字計數
wc ={} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增key進字典

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('想查詢甚麼? ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('沒有出現在字典裡喔!')
print('感謝使用查詢功能')

