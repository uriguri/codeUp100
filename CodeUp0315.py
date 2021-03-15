#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
2021 - 03 - 14 
아래의 코드들은 코드업 문제집 기초 100제의 문제들 입니다.
전 문제 코드업에서 정확한 풀이 채점을 받은 풀이 입니다.
"""

# 6008번 문제
# print("Hello\nWorld")
# 위 코드를 정확히 그대로 출력하시오.(공백문자 주의)

print(' print("Hello\\nWorld") ');


# In[2]:


# 6009번 문제 
# 변수에 문자 1개를 저장한 후
# 변수에 저장되어 있는 문자를 그대로 출력해보자.

uri = input();
print(uri);


# In[8]:


# 6010번 문제
# 변수에 정수값을 저장한 후
# 변수에 저장되어 있는 값을 그대로 출력해보자.

uri = input();
print (uri);


# In[13]:


# 6011번 문제
# 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

han = input();
uri = input();
print (han);
print (uri);


# In[20]:


# 6012번 문제
# 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

han = input();
uri = input();

print(uri);
print(han);


# In[25]:


# 6013번 문제
# 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

uri = input();

print(uri);
print(uri);
print(uri);


# In[27]:


# 6014번 문제
# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

'''
python의 input()은 한 줄 단위로 입력을 받는다.
input().split() 를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다.
'''

han,uri = input().split();
print(han);
print(uri);


# In[28]:


# 6015번 문제 
# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.
uri,han = input().split();

print(han);
print(uri);


# In[30]:


# 6016번 문제
# 정수(integer), 실수, 문자(character), 문자열(string) 등 
# 1개만 입력받아 한 줄로 3번 출력해보자.

uri = input();
print(uri,uri,uri);


# In[32]:


# 6017번 문제
# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

hour,minute = input().split(':');

print(hour,minute,sep=':');

# sep 는 분류기호(seperator)를 의미한다.


# In[34]:


# 6018번 문제
# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

y,m,d = input().split('.');
print(d,m,y,sep='-');


# In[37]:


# 6019번 문제
# 주민번호는 다음과 같이 구성된다.XXXXXX-XXXXXXX
# 주민번호를 입력받아 형태를 바꿔 출력해보자.

# '-'를 제외한 주민번호 13자리를 모두 붙여 출력한다.

person_num_f, person_num_s = input().split('-');
print(person_num_f,person_num_s,sep='');


# In[40]:


# 6020번 문제
# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

uri = input();
print(uri[0]);
print(uri[1]);
print(uri[2]);


# In[3]:


# 6021번 문제
# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

uri = input();
print(uri[0:2]);
print(uri[2:4]);
print(uri[4:6]);
print(uri[0:2],uri[2:4],uri[4:6]);


# In[4]:


# 6022번 문제
#시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

uri = input().split(':');
print(uri[1]);


# In[5]:


# 6023번 문제
# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
# 순서대로 붙여 출력하는 프로그램을 작성해보자.

han,uri = input().split();
han_uri = han + uri;
print(han_uri);


# In[52]:


# 6024번 문제
# 정수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.
# 공백을 두고 입력된다.

han,uri = input().split();
han_uri = int(han)+int(uri);
print(han_uri);


# In[6]:


# 6025번 문제
# 실수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.
# 줄을 바꿔 입력된다.

han = input();
uri = input();

han_uri = float(han)+float(uri);

print(han_uri);


# In[7]:


# 6026번 문제
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

# x = 소문자 형태로 출력
han = input();
uri = int(han);
print('%x'% uri);


# In[8]:


# 6027번 문제 
# X = 대문자 형태로 출력
han = input();
uri = int(han);
print('%X'% uri);


# In[9]:


# 6028번 문제 
# 16진수를 입력받아 8진수(octal)로 출력해보자.

a = input();

b = int(a,16);

print('%o' %b);


# In[11]:


# 6029번 문제
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.

han = ord(input());
print(han);


# In[12]:


# 6030번 문제
#10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.

han = int(input());

print(chr(han));


# In[16]:


# 6031번 문제
# 입력된 정수의 부호를 바꿔 출력해보자.

n = input();
print(-int(n));


# In[21]:


# 6032번 문제
# 문자 1개를 입력받아 그 다음 문자를 출력해보자.

han = ord(input());

print(chr(han+1));


# In[26]:


# 6033번 문제
# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력해보자.

a,b = input().split();

result = int(a) - int(b);

print(result);


# In[27]:


# 6034번 문제
# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

f1,f2 = input().split();

result = float(f1)*float(f2);

print(result);


# In[28]:


# 6035번 문제
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

han,uri = input().split();
print(han*int(uri));


# In[30]:


# 6036번 문제
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.
# 입력은 따로 받기로 한다.
re_num = input();
re_word = input();

print(int(re_num)*re_word);


# In[32]:


# 6037번 문제
# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

a,b = input().split();

print(int(a)**int(b));


# In[34]:


# 6038번 문제
# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

f1,f2 = input().split();

print(float(f1)**float(f2));


# In[37]:


# 6040번 문제
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

a,b = input().split();

print(int(a)//int(b));

# / 일반 나누기
# // 몫 구하기 
# % 나머지 구하기


# In[38]:


# 6041번 문제
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

a,b = input().split();

print(int(a)%int(b));


# In[40]:


# 6042번 문제
# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

han = input();

print(round(float(han),2));


# In[43]:


# 6043번 문제
# 실수 2개(f1, f2)를 입력받아 f1 을 f2 로 나눈 값을 출력해보자. 
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

f1,f2 = input().split();

result = float(f1)/float(f2);

print('%.3f'%result);


# In[46]:


# 6044번 문제
# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 
# 자동으로 계산해보자.

# 여섯 번째 줄에 나눈 값을 순서대로 출력한다.
# (실수, 소수점 이하 둘째 자리까지의 정확도로 출력)

a,b = input().split();
result_a = int(a);
result_b = int(b);

print(result_a+result_b);
print(result_a-result_b);
print(result_a*result_b);
print(result_a//result_b);
print(result_a%result_b);
print(round(result_a/result_b,2));


# In[49]:


# 6045번 문제 
# 정수 3개를 입력받아 합과 평균을 출력해보자.

a,b,c = input().split();

result_a = int(a);
result_b = int(b);
result_c = int(c);

result_sum = result_a+result_b+result_c;

print(result_sum,round(result_sum/3,2));



"""
python 프로그래밍을 처음 배울 때 좋은 습관(단계)
1. 입력된 문자열을 정확하게 잘라낸다.
(공백, 줄바꿈, 구분문자 등에 따라 정확하게 잘라낸다.)

2. 잘라낸 데이터들을 데이터형에 맞게 변환해 변수에 저장한다. 
(정수, 실수, 문자, 문자열 등에 따라 정확하게 변환한다.)

3. 값을 저장했다가 다시 사용하기 위해, 변수를 이용해 값을 저장하고, 
변수를 이용해 계산을 한다.

4. 원하는 결과 값을 필요한 형태로 만들어 출력한다.
(공백, 줄바꿈, 구분자, 등에 따라 원하는 형태로 만들어 출력한다.)
"""




# In[51]:


# 6046번 문제
# 정수 1개를 입력받아 2배 곱해 출력해보자.

"""
2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
가장 오른쪽에 있는 1비트는 사라진다.

예시
n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

정수 10의 2진수 표현은 ... 1010 이다.
10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.
"""

han = input();

print(int(han)<<1);


# In[53]:


# 6047번 문제
# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

a,b = input().split();

print(int(a)<<int(b));


# In[73]:


# 6048번 문제
# 두 정수(a, b)를 입력받아 a가 b보다 작으면 True 를, 
# a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

result_a = int(a);

result_b = int(b);

print(result_a<result_b);


# In[76]:


# 6049번 문제
# 두 정수(a, b)를 입력받아 a와 b의 값이 같으면 True 를, 
# 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

result_a = int(a);
result_b = int(b);

print(result_a == result_b);


# In[81]:


# 6050번 문제
# 두 정수(a, b)를 입력받아 b의 값이 a의 값 보다 크거나 같으면 True 를, 
# 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

result_a = int(a);
result_b = int(b);

print(result_a<=result_b);


# In[83]:


# 6051번 문제
# 두 정수(a, b)를 입력받아 a의 값이 b의 값과 서로 다르면 True 를, 
# 같으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

result_a = int(a);
result_b = int(b);

print(result_a != result_b);


# In[91]:


# 6052번 문제
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
# 입력된 값이 0이면 False, 0이 아니면 True 를 출력한다.

han = input();

print(bool(int(han) != 0));


# In[93]:


# 6053번 문제
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.


han = input();

print(not bool(int(han)));


# In[96]:


# 6054번 문제
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

print(bool(int(a)) and bool(int(b)));


# In[97]:


# 6055번 문제
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

print(bool(int(a)) or bool(int(b)));


# In[98]:


# 6056번 문제
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

result_a = bool(int(a));

result_b = bool(int(b));


print((result_a and (not result_b)) or ((not result_a) and result_b));


# In[99]:


# 6057번 문제
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자

a,b = input().split();

result_a = bool(int(a));
result_b = bool(int(b));

print(result_a == result_b);


# In[109]:


# 6058번 문제
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split();

result_a = bool(int(a));
result_b = bool(int(b));

print(not (result_a) and not(result_b));


# In[111]:


# 6059번 문제
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.

han = input();

print(~int(han));

"""
** 비트단위(bitwise) 연산자는,
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
가 있다.

정수 n이라고 할 때,
~n = -n - 1
-n = ~n + 1 
"""


# In[113]:


# 6060번 문제
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.

a,b = input().split();

result_a = int(a);
result_b = int(b);

print(result_a & result_b);


"""
비트단위 and 연산은 두 비트열이 주어졌을 때,
둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3       : 00000000 00000000 00000000 00000011
5       : 00000000 00000000 00000000 00000101
3 & 5   : 00000000 00000000 00000000 00000001
이 된다.

"""


# In[115]:


# 6061번 문제
# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.

a,b = input().split();

result_a = int(a);
result_b = int(b);

print(result_a | result_b);

"""
비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.
3과 5가 입력되었을 때를 살펴보면
3      : 00000000 00000000 00000000 00000011
5      : 00000000 00000000 00000000 00000101
3 | 5  : 00000000 00000000 00000000 00000111
이 된다.
"""


# In[116]:


# 6062번 문제
# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.

a,b = input().split();

result_a = int(a);
result_b = int(b);

print(result_a ^ result_b);

"""
예를 들어 3과 5가 입력되었을 때를 살펴보면
3       : 00000000 00000000 00000000 00000011
5       : 00000000 00000000 00000000 00000101
3 ^ 5 : 00000000 00000000 00000000 00000110
이 된다.
"""


# In[118]:


# 6063번 문제
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a,b = input().split();

result_a = int(a);
result_b = int(b);

result = (result_a if (result_a>=result_b) else result_b)

print(int(result));


# In[126]:


# 6064번 문제
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a,b,c = input().split();

result_a = int(a);
result_b = int(b);
result_c = int(c);

result = (result_b if result_a>result_b else result_a) if ((result_b if result_a>result_b else result_a)<result_c) else c 

print(int(result));


# In[3]:


# 6065번 문제
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a,b,c = input().split();

result_a = int(a);
result_b = int(b);
result_c = int(c);

if result_a%2 == 0 :
    print(a);
if result_b%2 == 0 :
    print(b);
if result_c%2 == 0 :
    print(c);


# In[4]:


# 6066번 문제
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a,b,c = input().split();

result_a = int(a);
result_b = int(b);
result_c = int(c);

if result_a % 2 == 0:
    print("even");
else :
    print("odd");

if result_b % 2 == 0:
    print("even");
else :
    print("odd");
    
if result_c % 2 == 0:
    print("even");
else :
    print("odd");


# In[8]:


# 6067번 문제
# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C 양수이면서 홀수이면, D 를 출력한다.

a = input();

n = int(a);

if n<0:
    if n%2 == 0:
        print('A');
    else :
        print('B');
else :
    if n%2 == 0:
        print('C');
    else :
        print('D');
        


# In[11]:


# 6068번 문제
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 평가 기준
# 점수 범위 : 평가
# 90 ~ 100 : A
# 70 ~   89 : B
# 40 ~   69 : C
#  0 ~   39 : D
# 로 평가되어야 한다.

a = input();

n = int(a);

if n>=90:
    print('A');
else :
    if n>=70:
        print('B');
    else :
        if n>=40:
            print('C');
        else :
            print('D');

################# elif 사용            
if n>=90:
    print('A');
elif n>=70:
    print('B');
elif n>=40:
    print('C');
else :
    print('D');
    


# In[12]:


# 6069번 문제
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

n = input();

if n == 'A' :
    print("best!!!");
elif n == 'B' :
    print("good!!");
elif n == 'C' :
    print("run!");
elif n == 'D' :
    print("slowly~");
else :
    print("what?");


# In[15]:


# 6070번 문제
# 월이 입력될 때 계절 이름이 출력되도록 해보자.

month = input();

n = int(month);

if 0<n<3 :
    print("winter");
elif 2<n<6 :
    print("spring");
elif 5<n<9 :
    print("summer");
elif 8<n<12 :
    print ("fall");
else :
    print("winter");
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




