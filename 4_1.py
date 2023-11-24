import xlrd
import matplotlib.pyplot as plt
import os

def read_excel(path):
    workbook = xlrd.open_workbook(path)
    sheet1_name = workbook.sheet_names()[0]
    sheet1 = workbook.sheet_by_name(sheet1_name)
    rows_list = [sheet1.row_values(i) for i in range(sheet1.nrows)]
    return rows_list

def process_data(row_list):
    emergency_male_count = 0
    emergency_female_count = 0
    total_visits = 0
    visits_per_department = {}

    for row in row_list[1:]:
        if row[3] == 'ED':
            if row[1] == 'boy':
                emergency_male_count += 1
            elif row[1] == 'girl':
                emergency_female_count += 1
        total_visits += 1
        department = row[3]
        visits_per_department[department] = visits_per_department.get(department, 0) + 1
    
    print(f"近五天急诊科男性就诊人数：{emergency_male_count}")
    print(f"近五天急诊科女性就诊人数：{emergency_female_count}")
    print(f"近五天来医院就诊的总人数：{total_visits}")
    print("近五天每个诊室就诊人数：")
    for department, count in visits_per_department.items():
        print(f"{department}：{count}")
    
    return emergency_male_count, emergency_female_count, total_visits, visits_per_department

def generate_emergency_gender_ratio_pie_chart(emergency_male_count, emergency_female_count, save_path):
    labels = ['Male', 'Female']
    sizes = [emergency_male_count, emergency_female_count]
    colors = ['skyblue', 'lightcoral']
    explode = (0, 0.1)
    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    
    plt.savefig(save_path)
    plt.show()

def generate_department_visits_bar_chart(visits_per_department, save_path):
    plt.figure(figsize=(10, 6))
    plt.bar(visits_per_department.keys(), visits_per_department.values(), color='skyblue')
    plt.xlabel('Consulting Room')
    plt.ylabel('Number of Visits')
    plt.title('Number of Visits per Consulting Room')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def generate_total_visits_line_chart(visits_per_day, save_path):
    sorted_dates = sorted(visits_per_day.keys())
    sorted_visits = [visits_per_day[date] for date in sorted_dates]

    plt.figure(figsize=(10, 6))
    plt.plot(sorted_dates[:-1], sorted_visits[:-1], marker='o', linestyle='-', color='skyblue')
    plt.xlabel('Day')
    plt.ylabel('Number')
    plt.title('The number of people who came to the hospital in the last five days')

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

def main():
    root_path = '/home/tione/notebook/任务四'
    excel_path = os.path.join(root_path,'赛位号_ hosptial.xls')
    row_list = read_excel(excel_path)

    emergency_male_count, emergency_female_count, total_visits, visits_per_department = process_data(row_list)
    generate_emergency_gender_ratio_pie_chart(emergency_male_count, emergency_female_count, 'emergency_gender_ratio_pie_chart.png')
    generate_department_visits_bar_chart(visits_per_department, 'department_visits_bar_chart.png')

    visits_per_day = {}
    for row in row_list:
        date_str = row[4]
        visits_per_day[date_str] = visits_per_day.get(date_str, 0) + 1
    
    generate_total_visits_line_chart(visits_per_day, 'total_visits_line_chart.png')

if __name__ == "__main__":
    main()
