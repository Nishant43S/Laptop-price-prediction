class LaptopFeatures:
  def Company_Name_Index(self,company):
    self.company = company
    self.company_dict = {
        "Acer": 0, "Apple": 1, "Asus": 2, "Chuwi": 3, "Dell": 4,
        "Fujitsu": 5, "Google": 6, "HP": 7, "Huawei": 8, "LG": 9,
        "Lenovo": 10, "MSI": 11, "Mediacom": 12, "Microsoft": 13, "Razer": 14,
        "Samsung": 15, "Toshiba": 16, "Vero": 17, "Xiaomi": 18
    }
    return self.company_dict[company]
  
  def Company_Name(self):
    self.company_dict_name = {
        "Acer": 0, "Apple": 1, "Asus": 2, "Chuwi": 3, "Dell": 4,
        "Fujitsu": 5, "Google": 6, "HP": 7, "Huawei": 8, "LG": 9,
        "Lenovo": 10, "MSI": 11, "Mediacom": 12, "Microsoft": 13, "Razer": 14,
        "Samsung": 15, "Toshiba": 16, "Vero": 17, "Xiaomi": 18
    }
    return self.company_dict_name.keys()
  
 
  def get_device_type_index(self,device_type):
    self.device_type = device_type
    self.device_type_dict = {
        "2 in 1 Convertible": 0, "Gaming": 1, "Netbook": 2, "Notebook": 3,
        "Ultrabook": 4, "Workstation": 5
    }
    return self.device_type_dict[device_type]

  def get_device_type(self):
    self.device_type_name =  {
        "2 in 1 Convertible": 0, "Gaming": 1, "Netbook": 2, "Notebook": 3,
        "Ultrabook": 4, "Workstation": 5
    }
    return self.device_type_name.keys()
  
  def get_os_index(self,os_name):
    self.os_name = os_name
    self.os_dict = {
        "Android": 0, "Chrome OS": 1, "Linux": 2, "Mac OS X": 3, "No OS": 4,
        "Windows 10": 5, "Windows 10 S": 6, "Windows 7": 7, "macOS": 8
    }
    return self.os_dict[os_name] 
  
  def get_os(self):
    self.os_dict_name = {
        "Android": 0, "Chrome OS": 1, "Linux": 2, "Mac OS X": 3, "No OS": 4,
        "Windows 10": 5, "Windows 10 S": 6, "Windows 7": 7, "macOS": 8
    }
    return self.os_dict_name.keys()
  


  def get_display_resolution_index(self,resolution):
      self.resolution = resolution
      self.resolution_dict = {
          "4K Ultra HD": 0, "Full HD": 1, "Quad HD+": 2, "Standard": 3
      }
      return self.resolution_dict[resolution]

  def get_display_resolution(self):
      self.resolution_type = {
          "4K Ultra HD": 0, "Full HD": 1, "Quad HD+": 2, "Standard": 3
      }
      return self.resolution_type.keys()

  

  def Touch_Screen(self,touchscreen):
    self.touchscreen = touchscreen
    if touchscreen == "Yes":
      return 1
    elif touchscreen == "No":
      return 0

  def IPS_panel(self,ips_panel):
    self.ips_panel = ips_panel
    if self.ips_panel == "Yes":
      return 1
    elif self.ips_panel == "No":
      return 0

  def Retina_Display(self,retina_display):
    self.retina_display = retina_display
    if self.retina_display == "Yes":
      return 1
    elif self.retina_display == "No":
      return 0

  def CPU_Company(self,cpu_company):
    self.cpu_company = cpu_company
    if self.cpu_company == "AMD":
      return 0
    elif self.cpu_company == "Intel":
      return 1
    elif self.cpu_company == "Samsung":
      return 2

  
  def get_cpu_model_index(self,cpu_model):
    self.cpu_model = cpu_model
    self.cpu_model_dict = {
        "A10-Series 9600P": 0, "A10-Series 9620P": 1, "A10-Series A10-9620P": 2,
        "A12-Series 9700P": 3, "A12-Series 9720P": 4, "A4-Series 7210": 5,
        "A6-Series 7310": 6, "A6-Series 9220": 7, "A6-Series A6-9220": 8,
        "A8-Series 7410": 9, "A9-Series 9410": 10, "A9-Series 9420": 11,
        "A9-Series A9-9420": 12, "Atom X5-Z8350": 13, "Atom Z8350": 14,
        "Atom x5-Z8300": 15, "Atom x5-Z8350": 16, "Atom x5-Z8550": 17,
        "Celeron Dual Core 3205U": 18, "Celeron Dual Core 3855U": 19,
        "Celeron Dual Core N3050": 20, "Celeron Dual Core N3060": 21,
        "Celeron Dual Core N3350": 22, "Celeron Quad Core N3160": 23,
        "Celeron Quad Core N3450": 24, "Celeron Quad Core N3710": 25,
        "Core M": 26, "Core M 6Y30": 27, "Core M 6Y54": 28, "Core M 6Y75": 29,
        "Core M 7Y30": 30, "Core M M3-6Y30": 31, "Core M M7-6Y75": 32,
        "Core M m3": 33, "Core M m3-7Y30": 34, "Core M m7-6Y75": 35,
        "Core i3 6006U": 36, "Core i3 6100U": 37, "Core i3 7100U": 38,
        "Core i3 7130U": 39, "Core i5": 40, "Core i5 6200U": 41,
        "Core i5 6260U": 42, "Core i5 6300HQ": 43, "Core i5 6300U": 44,
        "Core i5 6440HQ": 45, "Core i5 7200U": 46, "Core i5 7300HQ": 47,
        "Core i5 7300U": 48, "Core i5 7440HQ": 49, "Core i5 7500U": 50,
        "Core i5 7Y54": 51, "Core i5 7Y57": 52, "Core i5 8250U": 53,
        "Core i7": 54, "Core i7 6500U": 55, "Core i7 6560U": 56,
        "Core i7 6600U": 57, "Core i7 6700HQ": 58, "Core i7 6820HK": 59,
        "Core i7 6820HQ": 60, "Core i7 6920HQ": 61, "Core i7 7500U": 62,
        "Core i7 7560U": 63, "Core i7 7600U": 64, "Core i7 7660U": 65,
        "Core i7 7700HQ": 66, "Core i7 7820HK": 67, "Core i7 7820HQ": 68,
        "Core i7 7Y75": 69, "Core i7 8550U": 70, "Core i7 8650U": 71,
        "Cortex A72&A53": 72, "E-Series 6110": 73, "E-Series 7110": 74,
        "E-Series 9000": 75, "E-Series 9000e": 76, "E-Series E2-6110": 77,
        "E-Series E2-9000": 78, "E-Series E2-9000e": 79, "FX 8800P": 80,
        "FX 9830P": 81, "Pentium Dual Core 4405U": 82, "Pentium Dual Core 4405Y": 83,
        "Pentium Dual Core N4200": 84, "Pentium Quad Core N3700": 85,
        "Pentium Quad Core N3710": 86, "Pentium Quad Core N4200": 87,
        "Ryzen 1600": 88, "Ryzen 1700": 89, "Xeon E3-1505M V6": 90,
        "Xeon E3-1535M v5": 91, "Xeon E3-1535M v6": 92
    }
    return self.cpu_model_dict.get(cpu_model, -1)

  
  def CPU_Model_Name(self):
    self.cpu_model_name = {
        "A10-Series 9600P": 0, "A10-Series 9620P": 1, "A10-Series A10-9620P": 2,
        "A12-Series 9700P": 3, "A12-Series 9720P": 4, "A4-Series 7210": 5,
        "A6-Series 7310": 6, "A6-Series 9220": 7, "A6-Series A6-9220": 8,
        "A8-Series 7410": 9, "A9-Series 9410": 10, "A9-Series 9420": 11,
        "A9-Series A9-9420": 12, "Atom X5-Z8350": 13, "Atom Z8350": 14,
        "Atom x5-Z8300": 15, "Atom x5-Z8350": 16, "Atom x5-Z8550": 17,
        "Celeron Dual Core 3205U": 18, "Celeron Dual Core 3855U": 19,
        "Celeron Dual Core N3050": 20, "Celeron Dual Core N3060": 21,
        "Celeron Dual Core N3350": 22, "Celeron Quad Core N3160": 23,
        "Celeron Quad Core N3450": 24, "Celeron Quad Core N3710": 25,
        "Core M": 26, "Core M 6Y30": 27, "Core M 6Y54": 28, "Core M 6Y75": 29,
        "Core M 7Y30": 30, "Core M M3-6Y30": 31, "Core M M7-6Y75": 32,
        "Core M m3": 33, "Core M m3-7Y30": 34, "Core M m7-6Y75": 35,
        "Core i3 6006U": 36, "Core i3 6100U": 37, "Core i3 7100U": 38,
        "Core i3 7130U": 39, "Core i5": 40, "Core i5 6200U": 41,
        "Core i5 6260U": 42, "Core i5 6300HQ": 43, "Core i5 6300U": 44,
        "Core i5 6440HQ": 45, "Core i5 7200U": 46, "Core i5 7300HQ": 47,
        "Core i5 7300U": 48, "Core i5 7440HQ": 49, "Core i5 7500U": 50,
        "Core i5 7Y54": 51, "Core i5 7Y57": 52, "Core i5 8250U": 53,
        "Core i7": 54, "Core i7 6500U": 55, "Core i7 6560U": 56,
        "Core i7 6600U": 57, "Core i7 6700HQ": 58, "Core i7 6820HK": 59,
        "Core i7 6820HQ": 60, "Core i7 6920HQ": 61, "Core i7 7500U": 62,
        "Core i7 7560U": 63, "Core i7 7600U": 64, "Core i7 7660U": 65,
        "Core i7 7700HQ": 66, "Core i7 7820HK": 67, "Core i7 7820HQ": 68,
        "Core i7 7Y75": 69, "Core i7 8550U": 70, "Core i7 8650U": 71,
        "Cortex A72&A53": 72, "E-Series 6110": 73, "E-Series 7110": 74,
        "E-Series 9000": 75, "E-Series 9000e": 76, "E-Series E2-6110": 77,
        "E-Series E2-9000": 78, "E-Series E2-9000e": 79, "FX 8800P": 80,
        "FX 9830P": 81, "Pentium Dual Core 4405U": 82, "Pentium Dual Core 4405Y": 83,
        "Pentium Dual Core N4200": 84, "Pentium Quad Core N3700": 85,
        "Pentium Quad Core N3710": 86, "Pentium Quad Core N4200": 87,
        "Ryzen 1600": 88, "Ryzen 1700": 89, "Xeon E3-1505M V6": 90,
        "Xeon E3-1535M v5": 91, "Xeon E3-1535M v6": 92
    }
    return self.cpu_model_name.keys()
  
  def PrimararyStorageType_Index(self,P_storage):
    self.P_storage = P_storage

    self.P_storage_dict = {'Flash Storage':0,  'HDD':1, 'Hybrid':2,  'SSD':3}
    return self.P_storage_dict[P_storage]
  
  def PrimararyStorageType_Name(self):
    self.P_storage_name = {'Flash Storage':0,  'HDD':1, 'Hybrid':2,  'SSD':3}
    return self.P_storage_name.keys()
  
  def SecondaryStorageType_Index(self,S_storage):
    self.S_storage = S_storage

    self.S_storage_dict = {'HDD':0, 'Hybrid':1, 'No':2, 'SSD':3}
    return self.S_storage_dict[S_storage]
  
  def SecondaryStorageType_Name(self):
    
    self.S_storage_name = {'HDD':0, 'Hybrid':1, 'No':2, 'SSD':3}
    return self.S_storage_name.keys()
  
  def GPUCompany_Index(self,gpu_company):
    self.gpu_company = gpu_company

    self.gpu_company_dict = {'AMD':0,  'ARM':1,  'Intel':2,  'Nvidia':3}
    return self.gpu_company_dict[gpu_company]
  
  def GPUCompany_Name(self):
    self.gpu_type_name = {'AMD':0,  'ARM':1,  'Intel':2,  'Nvidia':3}
    return self.gpu_type_name.keys()
  
  def GPU_Model_Index(self,gpu_model):
    self.gpu_model = gpu_model

    self.gpu_model_dict = {'FirePro W4190M': 0, 'FirePro W4190M ': 1, 'FirePro W5130M': 2, 'FirePro W6150M': 3, 
                           'GTX 980 SLI': 4, 'GeForce 150MX': 5, 'GeForce 920': 6, 'GeForce 920M': 7, 'GeForce 920MX': 8, 
               'GeForce 920MX ': 9, 'GeForce 930M': 10, 'GeForce 930MX': 11, 'GeForce 930MX ': 12, 'GeForce 940M': 13,
                 'GeForce 940MX': 14, 'GeForce 960M': 15, 'GeForce GT 940MX': 16, 'GeForce GTX 1050': 17, 'GeForce GTX 1050 Ti': 18,
                   'GeForce GTX 1050M': 19, 'GeForce GTX 1050Ti': 20, 'GeForce GTX 1060': 21, 'GeForce GTX 1070': 22, 'GeForce GTX 1070M': 23, 
                   'GeForce GTX 1080': 24, 'GeForce GTX 930MX': 25, 'GeForce GTX 940M': 26, 'GeForce GTX 940MX': 27, 'GeForce GTX 950M': 28, 
        'GeForce GTX 960': 29, 'GeForce GTX 960<U+039C>': 30, 'GeForce GTX 960M': 31, 'GeForce GTX 965M': 32, 'GeForce GTX 970M': 33, 
        'GeForce GTX 980 ': 34, 'GeForce GTX 980M': 35, 'GeForce GTX1050 Ti': 36, 'GeForce GTX1060': 37, 'GeForce GTX1080': 38, 'GeForce MX130': 39,
          'GeForce MX150': 40, 'Graphics 620': 41, 'HD Graphics': 42, 'HD Graphics 400': 43, 'HD Graphics 405': 44, 'HD Graphics 500': 45, 
          'HD Graphics 505': 46, 'HD Graphics 510': 47, 'HD Graphics 515': 48, 'HD Graphics 520': 49, 'HD Graphics 530': 50, 'HD Graphics 5300': 51,
            'HD Graphics 540': 52, 'HD Graphics 6000': 53, 'HD Graphics 615': 54, 'HD Graphics 620': 55, 'HD Graphics 620 ': 56, 
            'HD Graphics 630': 57, 'Iris Graphics 540': 58, 'Iris Graphics 550': 59, 'Iris Plus Graphics 640': 60, 'Iris Plus Graphics 650': 61, 
            'Iris Pro Graphics': 62, 'Mali T860 MP4': 63, 'Quadro 3000M': 64, 'Quadro M1000M': 65, 'Quadro M1200': 66, 'Quadro M2000M': 67, 
            'Quadro M2200': 68, 'Quadro M2200M': 69, 'Quadro M3000M': 70, 'Quadro M500M': 71, 'Quadro M520M': 72, 'Quadro M620': 73,
              'Quadro M620M': 74, 'R17M-M1-70': 75, 'R4 Graphics': 76, 'Radeon 520': 77, 'Radeon 530': 78, 'Radeon 540': 79, 'Radeon Pro 455': 80,
                'Radeon Pro 555': 81, 'Radeon Pro 560': 82, 'Radeon R2': 83, 'Radeon R2 Graphics': 84, 'Radeon R3': 85, 'Radeon R4': 86, 
                'Radeon R4 Graphics': 87, 'Radeon R5': 88, 'Radeon R5 430': 89, 'Radeon R5 520': 90, 'Radeon R5 M315': 91, 'Radeon R5 M330': 92,
                  'Radeon R5 M420': 93, 'Radeon R5 M420X': 94, 'Radeon R5 M430': 95, 'Radeon R7': 96, 'Radeon R7 Graphics': 97, 'Radeon R7 M360': 98,
                    'Radeon R7 M365X': 99, 'Radeon R7 M440': 100, 'Radeon R7 M445': 101, 'Radeon R7 M460': 102, 'Radeon R7 M465': 103, 
                    'Radeon R9 M385': 104, 'Radeon RX 540': 105, 'Radeon RX 550': 106, 'Radeon RX 560': 107, 'Radeon RX 580': 108, 'UHD Graphics 620': 109
                    }
    return self.gpu_model_dict[gpu_model]
  
  def GPU_Model_Name(self):
    self.gpu_model_name =  {'FirePro W4190M': 0, 'FirePro W4190M ': 1, 'FirePro W5130M': 2, 'FirePro W6150M': 3, 
                           'GTX 980 SLI': 4, 'GeForce 150MX': 5, 'GeForce 920': 6, 'GeForce 920M': 7, 'GeForce 920MX': 8, 
               'GeForce 920MX ': 9, 'GeForce 930M': 10, 'GeForce 930MX': 11, 'GeForce 930MX ': 12, 'GeForce 940M': 13,
                 'GeForce 940MX': 14, 'GeForce 960M': 15, 'GeForce GT 940MX': 16, 'GeForce GTX 1050': 17, 'GeForce GTX 1050 Ti': 18,
                   'GeForce GTX 1050M': 19, 'GeForce GTX 1050Ti': 20, 'GeForce GTX 1060': 21, 'GeForce GTX 1070': 22, 'GeForce GTX 1070M': 23, 
                   'GeForce GTX 1080': 24, 'GeForce GTX 930MX': 25, 'GeForce GTX 940M': 26, 'GeForce GTX 940MX': 27, 'GeForce GTX 950M': 28, 
        'GeForce GTX 960': 29, 'GeForce GTX 960<U+039C>': 30, 'GeForce GTX 960M': 31, 'GeForce GTX 965M': 32, 'GeForce GTX 970M': 33, 
        'GeForce GTX 980 ': 34, 'GeForce GTX 980M': 35, 'GeForce GTX1050 Ti': 36, 'GeForce GTX1060': 37, 'GeForce GTX1080': 38, 'GeForce MX130': 39,
          'GeForce MX150': 40, 'Graphics 620': 41, 'HD Graphics': 42, 'HD Graphics 400': 43, 'HD Graphics 405': 44, 'HD Graphics 500': 45, 
          'HD Graphics 505': 46, 'HD Graphics 510': 47, 'HD Graphics 515': 48, 'HD Graphics 520': 49, 'HD Graphics 530': 50, 'HD Graphics 5300': 51,
            'HD Graphics 540': 52, 'HD Graphics 6000': 53, 'HD Graphics 615': 54, 'HD Graphics 620': 55, 'HD Graphics 620 ': 56, 
            'HD Graphics 630': 57, 'Iris Graphics 540': 58, 'Iris Graphics 550': 59, 'Iris Plus Graphics 640': 60, 'Iris Plus Graphics 650': 61, 
            'Iris Pro Graphics': 62, 'Mali T860 MP4': 63, 'Quadro 3000M': 64, 'Quadro M1000M': 65, 'Quadro M1200': 66, 'Quadro M2000M': 67, 
            'Quadro M2200': 68, 'Quadro M2200M': 69, 'Quadro M3000M': 70, 'Quadro M500M': 71, 'Quadro M520M': 72, 'Quadro M620': 73,
              'Quadro M620M': 74, 'R17M-M1-70': 75, 'R4 Graphics': 76, 'Radeon 520': 77, 'Radeon 530': 78, 'Radeon 540': 79, 'Radeon Pro 455': 80,
                'Radeon Pro 555': 81, 'Radeon Pro 560': 82, 'Radeon R2': 83, 'Radeon R2 Graphics': 84, 'Radeon R3': 85, 'Radeon R4': 86, 
                'Radeon R4 Graphics': 87, 'Radeon R5': 88, 'Radeon R5 430': 89, 'Radeon R5 520': 90, 'Radeon R5 M315': 91, 'Radeon R5 M330': 92,
                  'Radeon R5 M420': 93, 'Radeon R5 M420X': 94, 'Radeon R5 M430': 95, 'Radeon R7': 96, 'Radeon R7 Graphics': 97, 'Radeon R7 M360': 98,
                    'Radeon R7 M365X': 99, 'Radeon R7 M440': 100, 'Radeon R7 M445': 101, 'Radeon R7 M460': 102, 'Radeon R7 M465': 103, 
                    'Radeon R9 M385': 104, 'Radeon RX 540': 105, 'Radeon RX 550': 106, 'Radeon RX 560': 107, 'Radeon RX 580': 108, 'UHD Graphics 620': 109
                    }
    return self.gpu_model_name.keys()



