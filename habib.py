class _berat():
    def __init__(self, nama, tmpt_lahir, tgl_lahir, prodi, semester, kelas, gender, berat_badan, tinggi_badan,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.prodi = prodi
        self.semester = semester
        self.kelas = kelas
        self.gender = gender
        self.berat_badan = berat_badan
        self.tinggi_badan = tinggi_badan
        
    def _set (self, nama, tmpt_lahir, tgl_lahir,prodi, semester, gender, berat_badan, tinggi_badan,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.prodi = prodi
        self.semester = semester
        self.kelas = kelas
        self.gender = gender
        self.berat_badan = berat_badan
        self.tinggi_badan = tinggi_badan

    def _get (self):
        print('Nama lengkap   : ' + self.nama)
        print('TTL      : ' + self.tmpt_lahir + ', ' +  self.tgl_lahir)
        print('prodi  :' + self.prodi + ', ' + semester + ', ' + kelas)
        if self.gender in ['L', 'l']:
            gender = 'Laki-Laki'
        else:
            gender = 'Perempuan'
        print('Gender      :' + gender)

        if self.berat_badan >59:
            print('berat badan tidak normal')
        else:
            if self.berat_badan >56:
                print('berat badan normal')
            else:
                if self.berat_badan <56:
                    print('berat badan anak kecil')
             
        if self.tinggi_badan >170:
            print('tinggi badan tidak normal')
        else:
        	if self.tinggi_badan >160:
        	   print('tinggi badan normal')
        	else:
        	   if self.tinggi_badan <160:
        	       print('tinggi badan anak kecil')
        	       
print('========================================================')
print('     \tPROGRAM CEK TINGGI DAN BERAT BADAN      ')
print('========================================================')

nama      = input('Nama lengkap          :')
tmpt_lahir = input('Tempat lahir          :')
tgl_lahir  = input('Tanggal lahir         :')
prodi = input('prodi yang di pilih   :')
semester = input('semester              :')
kelas = input('masukan kelas         :')
gender     = input('Gender L/P            :')
berat_badan = float(input('Masukkan berat badan  :'))
tinggi_badan = float(input('masukan tinggi badan  :'))

print('========================================================')

proses = _berat(nama,tmpt_lahir,tgl_lahir,prodi,semester,kelas,gender,berat_badan,tinggi_badan)
print (proses._get())