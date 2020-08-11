from selenium import webdriver 

url = "https://capricho.abril.com.br/entretenimento/enquete-qual-dessas-10-comedias-romantica-e-a-sua-favorita-vote/"
browser = webdriver.Chrome() 
num = 0

while num < 5:
    browser.get(url) #abrindo url
    #escolhendo filme favorito
    favorite = browser.find_element_by_xpath('//*[@id="pds-answer10588949"]/div[2]/div/label/span') 
    favorite.click()
    #registrando voto
    vote = browser.find_element_by_xpath('//*[@id="pd-vote-button10588949"]/span') 
    vote.click()
    num+=1

