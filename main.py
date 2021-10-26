class Customer():# Customer için sınıf oluştuyorum.

    def __init__(self, input):

        index = 9999999#Input YazıSayı şeklinde olduğu için(a100, ali10, mert3 gibi) ilk gelen sayıynın indexi gerekiyor.
        for x in range(len(input)):
            if input[x] in ["0","1","2","3","4","5","6","7","8","9","0"]:
                index=x
                break
        if index==0:#Sadece sayı girilip isim girilmez ise faturalar isimsiz kullanıcı adı altında toplanıyor. Örn:22,10 gibi inputlar.
            self.name="İsimsizKullanıcı"
        else  :
            self.name = input[:index]#yazı kısmı name'e atanıyor.
        self.numberOfBill = int(input[index:])#sayı kısmı numberOfBill'e atanıyor.




def addToCustomerList(List,Customer): # Customerları sırasız bir şekilde toplamak için bir object list oluşturucu fonksiyon.
    newValue = True #girilen kullanıcının daha önce fatura girip girmediğini kontrol edecek booolean değer.
    indexNo=-1 #index tutacak.
    for x in List:
        if (x.name == Customer.name):#Elemanları kontrol edip isimleri aynı ise newValueyi false yapıyorum. Ve o ismin indexini tutuyorum.
            indexNo = List.index(x)
            newValue = False
            break

    if (newValue == False):#Eğer yeni kişi değilse eski faturalarının üstüne ekliyorum.

        List[indexNo].numberOfBill+=int(Customer.numberOfBill)
    else:#Yeni kişiyse direkt olarak listeye ekliyorum.
        List.append(Customer)



def addToQueue(customerlist):#Faturaları sırayla tek tek gösteren fonksiyon
    customerQueue = []#Sıralı liste
    copyList=customerlist.copy()#Esas listemizin değişmemesi için kopyası

    for counter in range(len(copyList)):#Listedeki elemanlar bitene kadar döndürmek için döngü
        maxBill=-1#En yüksek fatura sayısını bulma amacıyla bir değişken oluşturdum.
        index=-1
        maxCust=""
        for x in copyList:
            if maxBill <= x.numberOfBill:#En yüksek fatura sayısını gönderen kullanıcıyı bulana kadar geziyor.
                maxBill=x.numberOfBill
                maxCust=x#en yüksek faturalı Customer nesnesi tutuluyor.
                index=copyList.index(x)

        customerQueue.append(maxCust)#kuyruğun en arkasına ekleniyor
        copyList.pop(index)#en yüksek faturalı customer kopyalanmış listeden atılıyor kalanlarla aynı işlem tekrar yapılıyor.
    showQueue(customerQueue)#yazdırma fonksiyonu çağırılıyor


def showQueue(queue):#Kuyrukta tek tek gezip isimlerini ve fatura sayılarını yazdıran fonksiyon.
    for x in range(len(queue)):
        print("[",queue[x].name,queue[x].numberOfBill,"]",sep="",end=" ")
    print(">>>>> [Sunucu]")
    print()

def main():
    customerList=[]#Müşterilerin tutulacağı genel liste
    print("Müşteri bilgilerini giriniz.(Girdiğiniz bilgiler İsimFaturasayısı şeklinde olmalıdır. Örn:a100, ali20, mert10)(Çıkış için 0 giriniz)")
    info=input("İsimFatura:")
    print()

    while(info!="0"):
        try:
            customer=Customer(info)
            addToCustomerList(customerList,customer)
            addToQueue(customerList)
            print("Yeni müşteri girişi yapınız.(Çıkış için 0 giriniz)")
            info=input("İsimFatura:")
            print()
        except ValueError:
            print("Lütfen verilen formatta değer giriniz.")
            info = input("İsimFatura:")
            print()


main()