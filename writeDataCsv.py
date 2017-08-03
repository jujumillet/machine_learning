#X =[[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
#		[181, 85, 43], [173, 75, 43], [176, 62, 42], [156, 62, 37], [163, 55, 39],
#		[180, 72, 43], [187, 98, 45]]

#Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
#     'female', 'male', 'male', 'male', 'male', 'female', 'female', 'male', 'male']

w_file=open(os.path.join('test.csv'), 'w')
 
c = csv.writer(w_file, delimiter=';', lineterminator='\n')

c.writerow(X)
c.writerow(Y)
 
w_file.close()
del c