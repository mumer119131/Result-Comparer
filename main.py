import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



def highest_marks(result):
    no_of_items = len(result)
    highest_marks_holder = 0
    for i in range(0,no_of_items-1):
        if result[i][3]>result[highest_marks_holder][3]:
            highest_marks_holder = i
    print(result[highest_marks_holder][0]+" "+result[highest_marks_holder][1]+" have highest marks of "+result[highest_marks_holder][3]+" with grade "+result[highest_marks_holder][2])

url = "http://lms.uaf.edu.pk/login/index.php"

sub_name = input("Enter the name of the Subject : ").capitalize()
baseData={"2019-ag-6051": "FATIMA BASHIR", "2019-ag-6052": "ANIQA FAYYAZ", "2019-ag-6053": "AHTISHAM", "2019-ag-6054": "MUHAMMAD ABUBAKR", "2019-ag-6055": "JAHANZAIB BABAR", "2019-ag-6056": "MUHAMMAD SHOAIB AKBAR", "2019-ag-6057": "KHADIJAH RASOOL", "2019-ag-6058": "ANSA SALEEM", "2019-ag-6059": "ZUHA QAMMAR", "2019-ag-6060": "SYED ASAD ALI BUKHARI", "2019-ag-6061": "MUHAMMAD USAMA SHABIR", "2019-ag-6062": "MUHAMMADSHAHZAIB", "2019-ag-6063": "BUSHRA HAMEED", "2019-ag-6065": "HINA FAROOQ", "2019-ag-6066": "ASIMA SHABBIR", "2019-ag-6067": "MUHAMMAD KHAWAR AZEEM", "2019-ag-6068": "MUHAMMAD AHTESHAM SARWAR", "2019-ag-6069": "MAIRA", "2019-ag-6070": "MAKARAM TAYYAB", "2019-ag-6071": "ABDULLAH ALTAF", "2019-ag-6072": "TALHA AZEEM", "2019-ag-6073": "MUHAMMAD NOMAN", "2019-ag-6074": "TASBIHA TANVEER", "2019-ag-6075": "SHAFA ZAMAN", "2019-ag-6076": "ZOHA USMAN", "2019-ag-6077": "MISHAL JAVAID", "2019-ag-6078": "NABEEL UR REHMAN", "2019-ag-6079": "MUHAMMAD ZAIN", "2019-ag-6080": "LAIBA", "2019-ag-6081": "MUHAMMAD UMER", "2019-ag-6082": "MOHAMMAD RUMAN WARIS", "2019-ag-6084": "SAMIA TANVEER", "2019-ag-6085": "MANAL KHALID", "2019-ag-6086": "HAFIZA KHADIJA SULEMAN", "2019-ag-6087": "MUHAMMAD HASSAN KHALID", "2019-ag-6088": "AASHIR NADEEM", "2019-ag-6089": "MUHAMMAD HAMZA IMRAN BAJWA", "2019-ag-6090": "ADEEL AHMAD", "2019-ag-6091": "MUHAMMAD ABUBAKAR", "2017-ag-7217": "RANA TALHA", "2017-ag-7297":"Ahmed Raza"}
total_result = list()
driver=webdriver.Chrome(executable_path='F:\Outputs\Python Outputs\Web Scraping\Trying\chromedriver.exe')

driver.get(url)

for i in baseData:
    search_input = driver.find_element_by_id("REG")
    search_btn = driver.find_element_by_xpath("/html/body/div[3]/div/section/div/div/div/div[4]/div[1]/div[2]/div/div[1]/form/div[2]/input[3]")
    search_input.send_keys(i)
    ActionChains(driver).click(search_btn).perform()
    st_name = (driver.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td[2]")).text
    rows = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr"))
    cols = len(driver.find_elements_by_xpath("/html/body/table[2]/tbody/tr[2]/td"))
    for j in range(2,rows):
        sub_name_current = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(j)+"]/td[4]")).text
        if sub_name == sub_name_current:
            sub_marks = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(j)+"]/td[11]")).text
            sub_grade = (driver.find_element_by_xpath("/html/body/table[2]/tbody/tr["+str(j)+"]/td[12]")).text
            sub_result = list()
            sub_result.append(i)
            sub_result.append(st_name)
            sub_result.append(sub_grade)
            sub_result.append(sub_marks)
            total_result.append(sub_result)
            back_btn = driver.find_element_by_xpath("/html/body/a")
            ActionChains(driver).click(back_btn).perform()
            print(sub_result)
            break
driver.close()        
highest_marks(total_result)


def highest_marks(result):
    no_of_items = len(result)
    highest_marks_holder = 0
    for i in range(0,no_of_items-1):
        if result[i][3]>result[highest_marks_holder][3]:
            highest_marks_holder = i
    print(result[highest_marks_holder][0]+" "+result[highest_marks_holder][1]+" have highest marks of "+result[highest_marks_holder][3]+" with grade "+result[highest_marks_holder][2])        
            



