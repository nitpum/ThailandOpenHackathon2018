# ThailandOpenHackathon2018
โค้ดและโจทย์ทั้หมดจากงาน Thailand Open Hackathon 2018 ณ ศูนย์การประชุมแห่งชาติสิริกิติ์ วันอาทิตย์ที่ 4 พฤษภาคม พ.ศ. 2561
โค้ดทั้งหมดเขียนขึ้นโดยทีม**อะไรครับเนี่ย ! อ่านไม่ออก**

ในงานใช้ระบบ [DOMjudge](https://www.domjudge.org/) ในการตรวจสอบคำตอบ
รองรับภาษาทั้งหมด 3 ภาษาได้แก่ Java, C, Python3 โดยแต่ละภาษาใช้งานได้เฉพาะ library มาตรฐานเท่านั้น และส่งไฟล์ไปตรวจได้เพียงหนึ่งไฟล์ต่อหนึ่งรอบ

## กฎการแข่งขัน
[อ่านฉบับเต็ม](/q0/problem-0.pdf)

## โฟลเดอร์ | Folder Structure
- `q0/` โจทย์ตัวอย่าง เพื่อให้คนงานคุ้นเคยกับระบบตรวจคำตอบ
- `q1/`, `q2/`, `q3/`, `q4/`, `q5/` โจทย์ที่ใช้ในงาน โดยปล่อยออกมาทีละข้อมีระยะห่างแต่ละข้อประมาณ 40 นาที เพื่อความรวดเร็วในการทำงานจึงแบ่งไฟล์โค้ดของแต่ละคน โดยใช้ชื่อสมาชิกกำกับเพื่อบอกว่าใครเป็นคนเขียน
- `snippets/` โค้ดการใช้งาน python เบื้องต้นที่โหลดมาเตรียมไว้ก่อน ใช้เป็นแหล่งอ้างอิงในงานลดเวลาในการค้นหาจากอินเตอร์เน็ต

## ความต้องการของระบบ | Requirement
1. Python `3.8` ใช้ในการรันโปรแกรม
2. Git ใข้ในการเก็บรวบรวมและละแชร์ไฟล์ในงานได้อย่างสะดวก ([อ่านวิธีใช้งาน Git เบื้องต้น](https://devahoy.com/posts/introduction-to-git-and-github/))
3. Text Editor or IDE (Recommended VSCode with Python Extension) (ในงานสมาชิกทุกคนใช้โปรแกรม VSCode)
4. Brain
5. PC, Laptop, iPad, or anything that can run a Python


## วิธีใช้ Git Repo
คำสั่งพื้นฐานในการใช้งาน Git เพื่อความสะดวกในงานจะได้ไม่ต้องค้นหาคำสั่งการใช้งาน
### โหลดโปรเจคลงเครื่องครั้งแรก (ใช้แค่ครั้งเดียวตอนโหลดโปรเจคลงเครื่องเท่านั้น)
```
git clone https://github.com/nitpum/ThailandOpenHackathon2018.git
```
### ดานว์โหลดอัพเดทจากเซิฟเวอร์
```
git pull origin master
```
### บันทึกอัพเดทพร้อมใส่ข้อความการอัพเดท
```
git add --all
git commit -m "ใส่ข้อความอัพเดทภาษาอังกฤษ"
```
### อัพโหลดอัพเดทขึ้นเซิฟเวอร์เพื่อให้คนอื่นโหลดได้
```
git push origin master
```
### ซิงค์ข้อมูลจากเซิฟเวอร์ (โหลดอัพเดทมาลงเครื่องก่อน จากนั้นอัพโหลดอัพเดทในเครื่องขึ้นเซิฟเวอร์)
```
git pull origin master && git push origin master
```

# สมาชิกในทีม | Team Members 
ทีม: อะไรครับเนี่ย ! อ่านไม่ออก
(Ari Khrap Nia Ar Mai Okk)

Poom ([nitpum](https://github.com/nitpum]))

Arm ([topty](https://github.com/topty))

Kik ([yes2023](https://github.com/yes2023))

# License 
All source codes are Public domain
