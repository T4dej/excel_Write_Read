import openpyxl

original = "D:\\Programiranje\\Projekti\\junij01.xlsx"

wb_original = openpyxl.load_workbook(original)
original = wb_original.active
row_original = original.max_row

new_file = "D:\\Programiranje\\Projekti\\julij01.xlsx"

wb_file = openpyxl.load_workbook(new_file)
file = wb_file.active
row_file = file.max_row

for i in range(1, row_original + 1):
    data = file.cell(row = i, column=2)
    data_file = data.value
    data_1 = file.cell(row=i, column=3)
    data_value_1 = data_1.value
    for j in range(1, row_file + 1):
        data_original = original.cell(row = j, column=2)
        data_original_value = data_original.value
        if data_file == data_original_value:
            original.cell(row=j, column=5).value = data_value_1

        # to be continued...
        # else:
        #     original.append()

wb_original.save("test.xlsx")