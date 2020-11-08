import chromedriver_binary  ##これがあればchrome開ける
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import datetime


def buy_Betting():
    # パスワード/IDを下記に記載する必要があります
    # ボートレース
    boat_race_id = ""
    boat_race_password = ""
    boat_race_authPassword = ""
    boat_race_chargeBetPassword = ""
    # 楽天競馬
    rakuten_keiba_id = ""
    rakuten_keiba_password = ""
    rakuten_keiba_chargeBetPassword = ""
    # オートレース
    auto_race_userId = ""
    auto_race_password = ""
    auto_race_chargePassword = ""
    # ｅ－ＳＨＩＮＢＵＮ　ＢＥＴ
    shinbun_bet_id = ""
    shinbun_bet_password = ""
    shinbun_bet_chargeBetPassword = ""

    # チャリLOTO
    chari_loto_id = ""
    chari_loto_password = ""
    chari_loto_pincode = ""

    # 競輪
    keirin_jp_id = ""
    keirin_jp_password = ""
    keirin_jp_pincode = ""

    # オッズパーク
    oz_park_id = ""
    oz_park_password = ""
    oz_park_pin = ""

    # 南関東4競馬(SPAT4)
    SPAT4_keiba_member = ""
    SPAT4_keiba_id = ""
    SPAT4_keiba_pin = ""


    while_flag = True

    # # ヘッドレス処理
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)


    while_flag = True


    # ボートレース
    while while_flag:
        try:
            driver.get(
                "https://ib.mbrace.or.jp/")
            print("ボートレース画面")
            # ID/PASSを入力
            bord_id = driver.find_element_by_id("memberNo")
            bord_id.send_keys(boat_race_id)
            bord_password = driver.find_element_by_id("pin")
            bord_password.send_keys(boat_race_password)
            bord_authPassword = driver.find_element_by_id("authPassword")
            bord_authPassword.send_keys(boat_race_authPassword)
            login_button = driver.find_element_by_id("loginButton")
            login_button.click()

            WebDriverWait(driver, 3).until(lambda d: len(d.window_handles) > 1)
            driver.switch_to.window(driver.window_handles[1])

            # ログイン後
            driver.switch_to.window(driver.window_handles[-1])
            driver.implicitly_wait(10)  # 秒
            tab = driver.find_element_by_id("gnavi01")
            tab.click()
            charge = driver.find_element_by_id("charge")
            charge.click()
            money = driver.find_element_by_id("chargeInstructAmt")
            money.send_keys("1")
            chargeBetPassword = driver.find_element_by_id("chargeBetPassword")
            chargeBetPassword.send_keys(boat_race_chargeBetPassword)

            submit = driver.find_element_by_id("executeCharge")
            submit.click()

            submit_ok = driver.find_element_by_id("ok")
            submit_ok.click()
            sleep(3)
            driver.close()
            sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
        except NoSuchElementException:
            print('ボートレースエラー')
        finally:
            while_flag = False

    # 楽天競馬
    while_flag = True
    try:
        driver.get("https://bet.keiba.rakuten.co.jp/bank/deposit/")
        raku_id3 = driver.find_element_by_id("loginInner_u")
        raku_id3.send_keys(rakuten_keiba_id)
        raku_pass = driver.find_element_by_id("loginInner_p")
        raku_pass.send_keys(rakuten_keiba_password)
        login_button = driver.find_element_by_name("submit")
        login_button.click()

        # ログイン後
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(10)  # 秒
        price = driver.find_element_by_id("depositingInputPrice")
        price.send_keys("100")

        submit = driver.find_element_by_id("depositingInputButton")
        submit.click()

        sleep(1)

        password = driver.find_element_by_name("pin")
        password.send_keys(rakuten_keiba_chargeBetPassword)

        submit = driver.find_element_by_id("depositingConfirmButton")
        submit.click()

        sleep(1)

        driver.get("https://bet.keiba.rakuten.co.jp/bank/charge")

        chargeOrderInputButton = driver.find_element_by_id("chargeOrderInputButton")
        chargeOrderInputButton.click()

        password = driver.find_element_by_name("pin")
        password.send_keys(rakuten_keiba_chargeBetPassword)

        sleep(5)

        chargeOrderConfirmButton = driver.find_element_by_id(
            "chargeOrderConfirmButton")
        chargeOrderConfirmButton.click()

        sleep(3)
    except NoSuchElementException:
        print('楽天競馬エラー')
    finally:
        while_flag = False


    # オートレース
    while_flag = True
    try:
        driver.get("https://pc.autoinet.jp")
        autoinet_userId = driver.find_element_by_name("userId")
        autoinet_userId.send_keys(auto_race_userId)
        autoinet_password = driver.find_element_by_name("password")
        autoinet_password.send_keys(auto_race_password)

        autoinet_loginButton = driver.find_element_by_name("login")
        autoinet_loginButton.click()

        sleep(1)

        autoinet_passNo = driver.find_element_by_name("passNo")
        autoinet_passNo.send_keys(auto_race_chargePassword)

        autoinet_btnWireIn = driver.find_element_by_name("btnWireIn")
        autoinet_btnWireIn.click()

        sleep(1)

        autoinet_wireInAmount = driver.find_element_by_name("wireInAmount")
        autoinet_wireInAmount.send_keys('1')

        sleep(1)

        autoinet_refer = driver.find_element_by_name("refer")
        autoinet_refer.click()

        sleep(1)

        Alert(driver).accept()


    except NoSuchElementException:
        print('オートレースエラー')
    finally:
        while_flag = False


    # 南関東4競馬(SPAT4)
    while_flag = True
    try:
        driver.get("https://www.spat4.jp/keiba/pc")
        SPAT4_member = driver.find_element_by_id("MEMBERNUMR")
        SPAT4_member.send_keys(SPAT4_keiba_member)

        SPAT4_id = driver.find_element_by_id("MEMBERIDR")
        SPAT4_id.send_keys(SPAT4_keiba_id)


        SPAT4_loginButton = driver.find_element_by_xpath(
            "//a[@class='loginbtn easyhelp']//span")
        SPAT4_loginButton.click()

        sleep(1)

        SPAT4_loginButton = driver.find_element_by_id("goKaisai")
        SPAT4_loginButton.click()

        sleep(1)

        SPAT4_chargeButton = driver.find_element_by_xpath(
            "//input[@value='入金']")
        SPAT4_chargeButton.click()

        WebDriverWait(driver, 3).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])

        SPAT4_enterInput = driver.find_element_by_id("ENTERR")
        SPAT4_enterInput.send_keys(100)


        SPAT4_submitButton = driver.find_element_by_xpath(
            "//input[@value='入金指示確認へ']")
        SPAT4_submitButton.click()

        sleep(1)

        SPAT4_passInput = driver.find_element_by_id("MEMBERPASSR")
        SPAT4_passInput.send_keys(SPAT4_keiba_pin)

        sleep(1)

        SPAT4_submitButton = driver.find_element_by_name("EXEC")
        SPAT4_submitButton.click()

        sleep(1)

        driver.close()
        sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        sleep(1)

        SPAT4_payoffButton = driver.find_element_by_xpath(
            "//input[@value='精算']")
        SPAT4_payoffButton.click()

        sleep(1)

        SPAT4_payoffButton = driver.find_element_by_xpath(
            "//input[@value='精算指示確認へ']")
        SPAT4_payoffButton.click()

        sleep(1)

        SPAT4_passInput = driver.find_element_by_id("MEMBERPASSR")
        SPAT4_passInput.send_keys(SPAT4_keiba_pin)

        SPAT4_submitButton = driver.find_element_by_name("EXEC")
        SPAT4_submitButton.click()

    except NoSuchElementException:
        print('南関東4競馬エラー')
    finally:
        while_flag = False

    # オッズパーク
    while_flag = True
    try:
        driver.get("https://www.oddspark.com/")

        sleep(1)

        ozpark_id = driver.find_element_by_name("SSO_ACCOUNTID")
        ozpark_id.send_keys(oz_park_id)

        ozpark_pass = driver.find_element_by_name("SSO_PASSWORD")
        ozpark_pass.send_keys(oz_park_password)

        ozpark_loginButton = driver.find_element_by_id("btn_login")
        ozpark_loginButton.click()

        sleep(1)

        ozpark_pin = driver.find_element_by_name("INPUT_PIN")
        ozpark_pin.send_keys(oz_park_pin)

        ozpark_submit = driver.find_element_by_name("送信")
        ozpark_submit.click()

        sleep(1)

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        sleep(1)

        ozpark_chargeButton = driver.find_element_by_xpath(
            "//a[@class='nv5']")
        ozpark_chargeButton.click()

        sleep(1)

        WebDriverWait(driver, 3).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])

        ozpark_chargeButton = driver.find_element_by_xpath(
            "//li[@class='btn2']//a")
        ozpark_chargeButton.click()

        ozpark_money = driver.find_element_by_id("nyukin")
        ozpark_money.send_keys(1)

        sleep(1)

        ozpark_nextButton = driver.find_element_by_xpath(
            "//li[@class='btn2']//a")
        ozpark_nextButton.click()

        sleep(1)

        ozpark_pinpass = driver.find_element_by_id("touhyoPassword")
        ozpark_pinpass.send_keys(oz_park_pin)

        ozpark_nextButton = driver.find_element_by_xpath(
            "//li[@class='btn2']//a")
        ozpark_nextButton.click()

        sleep(1)

        ozpark_chargeButton = driver.find_element_by_xpath(
            "//a[@class='nv4']")
        ozpark_chargeButton.click()

        sleep(20)

        ozpark_chargeButton = driver.find_element_by_xpath(
            "//li[@class='btn2']//a[contains(text(), '精算する')]")
        ozpark_chargeButton.click()

        sleep(5)

        ozpark_pinpass = driver.find_element_by_id("touhyoPassword")
        ozpark_pinpass.send_keys(oz_park_pin)

        ozpark_nextButton = driver.find_element_by_xpath(
            "//li[@class='btn2']//a")
        ozpark_nextButton.click()

        driver.close()
        sleep(1)
        driver.switch_to.window(driver.window_handles[-1])

        sleep(1)
        print('オッズパーク完了')
    except NoSuchElementException:
        print('オッズパークエラー')
    finally:
        while_flag = False

    # ｅ－ＳＨＩＮＢＵＮ　ＢＥＴ
    while_flag = True
    check_error = False
    while while_flag:
        try:
            driver.get(
                "https://www.e-shinbun.net/account/?ref=ebet&path=http%3A%2F%2Fbet.e-shinbun.net%2F")

            sleep(1)

            shinbun_rakuten_userId = driver.find_element_by_xpath(
                "//input[@type='image']")
            shinbun_rakuten_userId.click()

            sleep(1)

            raku_id_2 = driver.find_element_by_id("loginInner_u")
            raku_id_2.send_keys(shinbun_bet_id)
            raku_pass = driver.find_element_by_id("loginInner_p")
            raku_pass.send_keys(shinbun_bet_password)
            login_button = driver.find_element_by_name("submit")
            login_button.click()

            sleep(10)
            driver.implicitly_wait(10)

            shinbun_continue = driver.find_element_by_xpath(
                "//div[@align='right']//a")
            shinbun_continue.click()

            driver.implicitly_wait(10)

            sleep(5)

            driver.get(
                "https://bet-core.e-shinbun.net/statements/deposit/")

            driver.implicitly_wait(10)

            shinbun_enter_money = driver.find_element_by_name("data[Statement][amount]")
            shinbun_enter_money.send_keys('100')

            shinbun_submit = driver.find_element_by_xpath(
                "//a[@class='std_btn']")
            shinbun_submit.click()

            sleep(1)

            shinbun_pass = driver.find_element_by_name("data[User][password]")
            shinbun_pass.send_keys(shinbun_bet_chargeBetPassword)

            shinbun_submit = driver.find_element_by_xpath(
                "//a[@class='left std_btn']")
            shinbun_submit.click()

            sleep(1)
            check_error = False
        except NoSuchElementException:
            print('ｅ－ＳＨＩＮＢＵＮ　ＢＥＴエラー')
            check_error = True
            driver.close()
            driver = webdriver.Chrome(options=chrome_options)
        finally:
            if check_error == False:
                while_flag = False
            print('ｅ－ＳＨＩＮＢＵＮ　ＢＥＴ終了')

    # - チャリLOTO
    while_flag = True
    check_error = False
    while while_flag:
        try:
            driver.get("https://www.chariloto.com/login")
            chariloto_id = driver.find_element_by_id("chariloto_id")
            chariloto_id.send_keys(chari_loto_id)

            chariloto_password = driver.find_element_by_id("password")
            chariloto_password.send_keys(chari_loto_password)


            chariloto_submit = driver.find_element_by_name("button")
            chariloto_submit.click()

            sleep(1)

            chariloto_nyukinButton = driver.find_element_by_xpath(
                "//a[@class='btn btn-base btn-small text-medium']")
            chariloto_nyukinButton.click()

            sleep(1)

            chariloto_money = driver.find_element_by_id("js-input")
            chariloto_money.send_keys('100')


            chariloto_commitButton = driver.find_element_by_name("commit")
            chariloto_commitButton.click()


            chariloto_pincode = driver.find_element_by_id(
                "mypage_bank_statement_deposit_form_pincode")
            chariloto_pincode.send_keys(chari_loto_pincode)

            chariloto_commitButton = driver.find_element_by_name("commit")
            chariloto_commitButton.click()

            #返金処理
            driver.get("https://www.chariloto.com/bank_statements/new_withdraw")

            sleep(1)

            chariloto_pass = driver.find_element_by_id(
                "mypage_bank_statement_withdrawal_form_pincode")
            chariloto_pass.send_keys(chari_loto_pincode)

            chariloto_commitButton = driver.find_element_by_name("commit")
            chariloto_commitButton.click()

            sleep(2)
            check_error = False
        except NoSuchElementException:
            print('チャリLOTOエラー')
            check_error = True
            driver.close()
            driver = webdriver.Chrome(options=chrome_options)
        finally:
            if check_error == False:
                while_flag = False
            print('チャリLOTO終了')


    # 競輪
    while_flag = True
    check_error = False
    while while_flag:
        try:
            driver.get("http://keirin.jp/pc/top")

            sleep(1)

            keirin_id = driver.find_element_by_id(
                "trtxtBallotID")
            keirin_id.send_keys(keirin_jp_id)

            keirin_pass = driver.find_element_by_id(
                "trtxtBallotPW")
            keirin_pass.send_keys(keirin_jp_password)

            keirin_loginButton = driver.find_element_by_xpath(
                "//input[@class='btn onbtn al-c login_keyicon']")
            keirin_loginButton.click()

            sleep(5)
            driver.implicitly_wait(10)


            keirin_enterButton = driver.find_elements_by_xpath(
                "//button[@class='btn onbtn'][contains(text(), '入　金')]")

            keirin_enterButton[0].click()

            sleep(3)
            driver.implicitly_wait(10)

            keirin_inputMoney = driver.find_element_by_id(
                "UNQ_orexpandText_12")
            keirin_inputMoney.send_keys("1")

            sleep(1)
            driver.implicitly_wait(10)

            keirin_submitButton = driver.find_element_by_id(
                "UNQ_orbutton_36")
            keirin_submitButton.click()

            sleep(1)
            driver.implicitly_wait(10)

            keirin_inputPass = driver.find_element_by_id(
                "UNQ_pfInputText_14")
            keirin_inputPass.send_keys(keirin_jp_pincode)

            sleep(2)
            driver.implicitly_wait(10)

            keirin_submitButton = driver.find_element_by_id(
                "UNQ_orbutton_18")
            keirin_submitButton.click()

            sleep(2)
            driver.implicitly_wait(10)

            keirin_payOffButton = driver.find_element_by_id(
                "UNQ_orbutton_6")
            keirin_payOffButton.click()

            sleep(1)

            check_error = False
        except NoSuchElementException:
            print('競輪エラー')
            check_error = True
            driver.close()
            driver = webdriver.Chrome(options=chrome_options)
            
        finally:
            print('競輪終了')
            if check_error == False:
                while_flag = False
                print('正常に終了')
                # ブラウザを終了する。
                driver.close()
                

set_time = int("1230")
dt = datetime.datetime.now()
time = int(dt.strftime("%H%M"))
count_flag = False
diff = 0

while True:
    # 時間確認
    if set_time < time:
        count_flag = True
        dt1 = datetime.datetime(dt.year, dt.month, dt.day, 12, 30, 0)
        dt2 = datetime.datetime.now()
        diff = (dt2 - dt1).seconds
    
    # 日付変わった＋時間が12:30以降の場合に実行
    if  count_flag:
        print('購入開始')
        buy_Betting()
        # day_reset = False
        count_flag = False
        dt = datetime.datetime.now()
        day = int(dt.strftime("%Y%m%d"))
        
    print('実行中')
    sleep(60 * 60 * 24 - diff)
    new_dt = datetime.datetime.now()
    time = int(new_dt.strftime("%H%M"))
    

print('end')