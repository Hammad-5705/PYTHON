import time

def fx():

    lvl=[
        1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,340000,1250000,2500000,500000,10000000
    ]

    ques=[

    [
        "1. Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?",
    "A. Solicitor General              B. Attorney General",
    "C. Cabinet Secretary              D. Chief Justice ",
    2
    ],
    [
        "2. Who, in 1978, became the first person to be born in the continent of Antarctica?",
    "A. Emilio Palma                   B. James Weddell", 
    "C. Nathaniel Palmer               D. Charles Wilkes",
    1
    ],

    [
    "3. Who, in 1978, became the first person to be born in the continent of Antarctica?",
    "A. Emilio Palma                    B. James Weddell",
    "C. Nathaniel Palmer                D. Charles Wilkes",
    3
    ],

    [
    "4. Who is the first woman to successfully climb K2, the world’s second highest mountain peak?",
    "A. Junko Tabei                     B. Wanda Rutkiewicz",
    "C. Tamae Watanabe                  D. Chantal Mauduit",
    2
    ],

    [
        "5. Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?",
    "A. Mir Taqi Mir                    B. Mohammad Ibrahim Zauq ",
    "C. Zahir Dehlvi                    D. Abul-Qasim Ferdowsi",
    3
    ],

    [
    "6. The historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were held at which place in Shimla?",
    "A. Viceregal Lodge                 B. Gorton Castle ",
    "C. Barnes Court                    D. Cecil Hotel",
    3
    ],

    [
    "7. Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?",
    "A. Cathay Cinema Hall                          B. Fort Canning Park ",
    "C. National University of Singapore            D. National Gallery of Singapore",
    1
    ],

    [
    "8. Milinda-Panha is a dialogue between King Menander or Milinda and which Buddhist monk?",
    "A. Asanga                          B. Nagasena",
    "C. Mahadharmarakshita              D. Dharmaraksita",
    2
    ],

    [
    "9. What was the title of the thesis that Dr. B. R. Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?",
    "A. The Want and Means of India                 B. The Problem of the Rupee",
    "C. National Dividend of India                  D. The Law and Lawyers",
    2
    ],

    [
    "10.    Which was the first mountain peak above 8,000 metres in height to be summited by humans?",
    "A. Annapurna                       B. Lhotse",
    "C. Kanchenjunga                    D. Makalu",
    1
    ],

    [
    "11.    According to the Padma Purana, which king had to live as a tiger for a hundred years due to a deer\'s curse?",
    "A. Kshemadhurti                    B. Dharmadatta",
    "C. Mitadhvaja                      D. Prabhanjana",
    4
    ],

    [
    "12.    Leena Gade, a person of Indian origin, is the first female race engineer to win which of the following races?",
    "A. Indianapolis 500                B. 24 Hours of Le Mans",
    "C. 12 Hours of Sebring             D. Monaco Grand Prix",
    2
    ],

    [
    "13.   ________ day is observed as World Standards Day.",
    "A. Nov 15                          B. Oct 14",
    "C. Dec 2                           D. June 26",
    2

    ],

    [
    "14.    The theme of the World Red Cross and Red Crescent Day was?",
    "A. Dignity for all – focus on Children                 B. Nourishment for all-focus on children",
    "C. Focus on health for all                             D. Dignity for all – focus on women",
    1
    ],

    [
    "15.    ________ is celebrated on September 27 every year.",
    "A. National Integration Day                        B. Teachers’ Day",
    "C. International Literacy Day                      D. World Tourism Day",
    4
    ],

    ]

    won=0

    for i in range(len(ques)):
        que=ques[i]

        for ii in range(len(que)):
            
            while(ii<3):
            
                if(ii==1):
                    print("\n")
            
                print(que[ii])
                break

            if(ii==2):
                try:
                    ans=int(input("\n Choose your Answer :"))
                    time.sleep(1)

                except:
                    print("Invalid Input")
                    raise ValueError("Invalid Input Please input 1,2,3 or 4")

        if(ans!=que[3]):
            # return won
            won=chk(won)
            return won
            
        else:
            won=lvl[i]
            print("\n\n\n")
            print("\033[32m your level =\033[0m",won )  
            print("\n")          
    
            
            

        


            
    # if(won<10000):
    #     return 0

    # elif(won>=10000 and won<320000):
    #     won=10000
    
    # elif(won>=320000 and won<10000000):
    #     won=320000
    
    return won

def chk(a):
    if(a<10000):
     return 0

    elif(a>=10000 and a<320000):
        a=10000
    
    elif(a>=320000 and a<10000000):
        a=320000
    
    return a
        

print("Welcome to Kon Bnyga Caror pati")

z=fx()

if(z>0):
    print("\033[32m You won\033[0m", z)  

else:
    print("\033[31m You won\033[0m", z)