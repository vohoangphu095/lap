'''
Cach lam:
-cho chuỗi alphabet vd từ a tới z
-nhập vi trí index vd abc
-nhập số  bước nhảy
-tạo list rỗng
b1 tạo hàm encrypt
    -vòng lặp for cho chuỗi ký tự thứ index nhập vào
    -nếu nhập ký tự trùng với ký tự trong alphabet
        -xác định vị trí tại vị trí index trong chuỗi alphabet
        -xác định vị trí nhảy tới từ index = vị trí index + số bước nhảy
        -thêm vào chuỗi trống đã tạo
b2 gọi hàm xuất ra
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

text = input("Nhập nội dung:\n").lower()
shift = int(input("Nhập số di chuyển:\n"))


def encrypt(text, shift):
    stri = ""
    for i in text:
        index = alphabet.index(i)
        shif_index = (index + shift) % len(alphabet)
        new_lett = alphabet[shif_index]
        stri += new_lett
    print(f'word after moved: {stri}')


encrypt(text=text, shift=shift)
