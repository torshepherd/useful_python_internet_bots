import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import signal
import sys

PATH = 'C:\Program Files (x86)\ChromeDriver\chromedriver.exe'

BB_LOGIN = os.environ.get('BB_LOGIN')
BB_PASS = os.environ.get('BB_PASS')
BB_CVV = os.environ.get('BB_CVV')

RTX_3060TI_FE_LINK = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
RTX_3070_FE_LINK = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442'
RTX_3070TI_FE_LINK = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-ti-8gb-gddr6x-pci-express-4-0-graphics-card-dark-platinum-and-black/6465789.p?skuId=6465789'
RTX_3070TI_PNY_LINK = 'https://www.bestbuy.com/site/pny-geforce-rtx-3070-ti-8gb-xlr8-gaming-revel-epic-x-rgb-triple-fan-graphics-card/6470355.p?cmp=RMX&refdomain=t.co&skuId=6470355'
RTX_3070TI_MSI_LINK = 'https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3070-ti-gaming-x-trio-8g-gddr6-pci-express-4-0-graphics-card/6467497.p?skuId=6467497'
RTX_3070TI_GIGABYTE_LINK = 'https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070ti-gaming-oc-8gb-gddr6x-pci-express-4-0-graphics-card-black/6467779.p?skuId=6467779'
RTX_3080_FE_LINK = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
RTX_3080_ASUS_LINK = 'https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445'
RTX_3080_GIGABYTE_LINK = 'https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-gaming-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6430620.p?skuId=6430620'
RTX_3080_GIGABYTE_VISION_LINK = 'https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-vision-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6436219.p?skuId=6436219'
RTX_3080_EVGA_LINK = 'https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400'
RTX_3080TI_FE_LINK = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956'
TEST_LINK = 'https://www.bestbuy.com/site/sony-43-class-x85j-4k-uhd-smart-google-tv/6459483.p?skuId=6459483'

# Remove or add links to this list to try to buy them
links_to_buy = [['RTX 3070 FE', RTX_3070_FE_LINK],
                ['RTX 3070 ti FE', RTX_3070TI_FE_LINK],
                ['RTX 3070 ti PNY', RTX_3070TI_PNY_LINK],
                ['RTX 3070 ti MSI', RTX_3070TI_MSI_LINK],
                ['RTX 3070 ti Gigabyte', RTX_3070TI_GIGABYTE_LINK],
                ['RTX 3080 FE', RTX_3080_FE_LINK],
                ['RTX 3080 ASUS', RTX_3080_ASUS_LINK],
                ['RTX 3080 Gigabyte', RTX_3080_GIGABYTE_LINK],
                ['RTX 3080 Gigabyte Vision', RTX_3080_GIGABYTE_VISION_LINK],
                ['RTX 3080 EVGA', RTX_3080_EVGA_LINK],
                ['RTX 3080 ASUS', RTX_3080_ASUS_LINK],
                ['RTX 3080 ti FE', RTX_3080TI_FE_LINK]]


def add_to_cart(browser, product_link):
    try:
        # Navigate to product page
        browser.get(product_link)

        # Click add to cart
        add_to_cart_button = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.add-to-cart-button'))
        )

        # add to cart
        add_to_cart_button.click()

        return True

    except KeyboardInterrupt:
        sys.exit(0)

    except:
        return False


def checkout_bestbuy_cart(browser):
    try:
        # Navigate to the checkout page
        browser.get('https://www.bestbuy.com/cart')

        # Check out
        checkoutBtn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'checkout-buttons__checkout'))
        )
        checkoutBtn.click()

        # Write in login info
        emailField = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(BB_LOGIN)
        pwField = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(BB_PASS)

        # Click sign in button
        signInBtn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[@type=\'submit\']'))
        )
        signInBtn.click()
        
        # fill in card cvv
        try:
            cvvField = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "credit-card-cvv"))
            )
            cvvField.send_keys(BB_CVV)
        except:
            pass
        
        # place order
        placeOrderBtn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
        )
        placeOrderBtn.click()

        return True

    except KeyboardInterrupt:
        print("here")
        sys.exit(0)
    
    except:
        return False

def buy_product(product_link):
    browser = webdriver.Chrome(PATH)
    success = False
    while not success:
        print('Trying to add {} to cart.'.format(product_link[0]))
        success = add_to_cart(browser, product_link[1])
        if success:
            print('Success! Checking out {}.'.format(product_link[0]))
            checkout_bestbuy_cart(browser)
        else:
            browser.refresh()
    return 'Completed {}.'.format(product_link[0])

def signal_handler():
    print("here")
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Loop version
    # browser = webdriver.Chrome(PATH)
    # success = False
    # while not success:
    #     for product_link in links_to_buy:
    #         print('Trying to add {} to cart.'.format(product_link[44:55]))
    #         success = add_to_cart(browser, product_link)
    #         if success:
    #             print('Success! Checking out')
    #             checkout_bestbuy_cart(browser)
    #             break

    # Parallel version
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for product_link in links_to_buy:
            futures.append(executor.submit(buy_product, product_link=product_link))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
