# นี่คือ code fibonacci แสนธรรมดา
# สร้างตัวนับ
count = 0

def fibo(n):
	if n == r:
		# ถ้า fibo(n) ตรงกับตัวที่เราจะนับให้ global แล้วเพิ่มค่าตัวนับไป 1
		# global คือการทำให้สามารถแก้ไขตัวแปรระดับ global ได้ อ่านเพิ่มในเรื่อง Global/Local Variable
		global count
		count += 1
	if n == 0:
		return
	if n == 1:
		return
	fibo(n-1)
	fibo(n-2)

f = input()
r = input()
fibo(f)
print count

# ปล. code นี้ส่งข้อ FibonacciSharp ไม่ผ่านนะจ๊ะ :P