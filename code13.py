#coding = utf-8
#ð������
#line 4:����һ��������б�list
array = [1,2,5,3,6,8,4]
'''line 7:������ϱ߸������ӵĵڶ����������滻�¾ͳ�Ϊrange(6,1,-1)����˼�Ǵ�6��1���-1,
Ҳ���ǵ����range(2,7,1),������Щֵѭ������i����ôi��ֵ������[6, 5, 4, 3, 2]'''
for i in range(len(array)-1,0,-1):
    print i
    #line 10:����һ��ѭ����ֵ��j��j��ֵ������[0, 1, 2, 3, 4, 5][0, 1, 2, 3, 4][0, 1, 2, 3][0, 1, 2][0, 1]'''
    for j in range(0,i):
        print j
        #line 13����ʵ������ʹ����������û��˳���array = [1, 2, 5, 3, 6, 8, 4]����'''
        if array[j] > array[j + 1]:
            #line 15��array[j], array[j + 1] = array[j + 1], array[j] �滻��ֵ'''
            array[j],array[j+1] = array[j+1],array[j]
            print 'i:',i, 'j:', j, '-->', array            
#print array


#map(function, sequence) Ϊÿһ��Ԫ�����ε��� function(item) ��������ֵ���һ��������
def cube(x): 
    print x*x*x

map(cube,range(1,11))

#�б��Ƶ�ʽΪ�������д����б��ṩ��һ���򵥵ķ�����
#��ͨ��Ӧ�ó���ͨ����һЩ����Ӧ�������е�ÿ����Ա��ͨ�����ص�Ԫ�ش����б�����ͨ�������ض�������Ԫ�ش���������
squares = []
for x in range(10):
    squares.append(x**2)
print squares



#ʹ��sortһ��Ϳ��Ը㶨
hp = [1,2,5,3,6,8,4]
hp.sort()
print hp