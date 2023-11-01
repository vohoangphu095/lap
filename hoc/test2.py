import seaborn as sns
import matplotlib.pyplot as plt

# Dữ liệu mẫu: phân bố của một biến số ngẫu nhiên
data1 = [3, 4, 6, 8, 9, 10, 12, 15, 17, 18, 20, 22, 23, 25, 27, 28, 30]
data2 = [5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]

# Tạo biểu đồ displot cho data1
sns.displot(data1, kde=True, color='blue')

plt.xlabel('Giá trị')
plt.ylabel('Số lượng')
plt.title('Phân bố đơn biến - Data 1')
plt.show()

# Tạo biểu đồ displot cho data2
sns.displot(data2, kde=True, color='red')

plt.xlabel('Giá trị')
plt.ylabel('Số lượng')
plt.title('Phân bố đơn biến - Data 2')
plt.show()
