from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import sys
import codecs
from random import randint

def find(find_results):
	if len(find_results) == 0:
		print 'Did not found a chat with that name. Ending execution...'
		sys.exit(0)
	else:
		return find_results

def load_text(file_name):
	f = codecs.open(file_name, encoding='utf-8')
	sentences = f.read().split('\n')
	return sentences, len(sentences)

def get_random(list, list_len):
	return list[randint(0, list_len-1)]

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print 'Usage: python whatsapp_spammer.py [victim_name] [spam_filename]'
	target_name = sys.argv[1]
	spam_sentences, spam_length = load_text(sys.argv[2])

	driver = webdriver.Firefox()
	driver.get('https://web.whatsapp.com')
	(driver.page_source).encode('utf-16')

	raw_input('Scan your QR Code and press enter when you can see your chat list...')

	input_fields = find(driver.find_elements_by_class_name("input"))
	search_contacts_field = input_fields[0]
	search_contacts_field.send_keys(target_name)

	spamming_target = find(driver.find_elements_by_xpath("//*[contains(text(), '%s')]" % (target_name)))
	spamming_target[0].click()

	time.sleep(2)

	input_fields = find(driver.find_elements_by_class_name("input"))
	type_text_field = input_fields[1]

	print 'Starting spam. Press CTRL+C to end execution.'
	try:
		while(1):
			type_text_field.send_keys(get_random(spam_sentences, spam_length))
			type_text_field.send_keys(Keys.RETURN)
	except Exception as e:
		print e
		print 'Ending execution.'

	driver.close()