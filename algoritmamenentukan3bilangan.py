Program Maksimum {Menentukan bilangan terbesar dari tiga bilangan}
Deklarasi:
  A, B, C, maks: integer
ALGORITMA:
  read(A,B,C)
  if A > B then
    maks  <-  A
  else
    maks  <-  B
  end if
  
  if maks < C then
     maks <- C
  end if
  
  write("terbesar",maks)