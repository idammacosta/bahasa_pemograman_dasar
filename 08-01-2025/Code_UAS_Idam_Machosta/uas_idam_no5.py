saldo_awal = 1000000
bunga_per_bulan = 0.02
bulan = 10

saldo = saldo_awal
for i in range(1, bulan + 1):
    saldo += saldo * bunga_per_bulan 
    print(f"Bulan ke-{i}: Rp. {saldo:,.2f}")

print(f"\nJumlah uang setelah {bulan} bulan: Rp. {saldo:,.2f}")