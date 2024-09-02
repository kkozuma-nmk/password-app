import random
import string

形容詞リスト = ['strong','happy','dry',
							'wet','hungry','red',
							'orange','yellow','green',
							'blue','gray','big',
							'white','kind','busy']
							
名詞リスト = ['apple','tiger','ball',
						'desk','goat','dragon',
						'piano','duck','panda',]
						
print('これからパスワードを生成します。')

while True:						

		形容詞 = random.choice(形容詞リスト)
		名詞 = random.choice(名詞リスト)
		数 = random.randrange(0,100)
		記号 = random.choice(string.punctuation)
		
		
		パスワード = 形容詞 + 名詞 + str(数) + 記号
		print('新しいパスワードは: %s' % パスワード + ' です。')
		
		
		回答 = input('他のパスワードにしたいですか？　yかnで答えてください。:')
		if 回答 == 'n':
				break