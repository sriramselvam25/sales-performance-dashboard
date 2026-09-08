"""Generate the Executive Sales Analytics synthetic portfolio dataset.
No employer or confidential data is used.
"""
from pathlib import Path
from datetime import date, timedelta
import csv, random
import numpy as np

SEED = 42
ROWS = 55_000
random.seed(SEED)
np.random.seed(SEED)
OUT = Path("generated")
OUT.mkdir(exist_ok=True)

geos = [
("GEO001","APAC","India"),("GEO002","APAC","Singapore"),("GEO003","APAC","Australia"),
("GEO004","Europe","Germany"),("GEO005","Europe","United Kingdom"),("GEO006","Europe","France"),
("GEO007","North America","United States"),("GEO008","North America","Canada"),
("GEO009","MEA","United Arab Emirates"),("GEO010","MEA","South Africa"),
("GEO011","Latin America","Brazil"),("GEO012","Latin America","Mexico")]
products = [
("PROD001","Home Care","Surface Cleaner 1L",185,121),("PROD002","Home Care","Laundry Liquid 2L",420,255),
("PROD003","Home Care","Dishwash Gel 750ml",230,139),("PROD004","Home Care","Floor Cleaner 1L",205,124),
("PROD005","Personal Care","Shampoo 400ml",390,230),("PROD006","Personal Care","Body Wash 500ml",350,210),
("PROD007","Personal Care","Hand Wash 250ml",160,96),("PROD008","Personal Care","Deodorant 150ml",280,220),
("PROD009","Food & Beverage","Instant Coffee 200g",540,310),("PROD010","Food & Beverage","Breakfast Cereal 500g",310,185),
("PROD011","Food & Beverage","Fruit Juice 1L",190,150),("PROD012","Food & Beverage","Green Tea 100pk",460,270),
("PROD013","Baby & Family","Baby Wipes 80pk",220,130),("PROD014","Baby & Family","Baby Lotion 200ml",280,165),
("PROD015","Baby & Family","Diapers M 40pk",760,610),("PROD016","Baby & Family","Tissues 10pk",260,150)]
channels=[("CH01","Distributor",.03),("CH02","Retail",.05),("CH03","Online",.10),("CH04","Direct B2B",.02)]
regions=["APAC","Europe","North America","MEA","Latin America"]
salespeople=[(f"SP{i+1:03d}",f"Salesperson {i+1:02d}",regions[i%5]) for i in range(20)]
segments=["Retail","SMB","Enterprise","Distributor"]

# Dimensions
with open(OUT/"DimGeography.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["GeographyID","Region","Country"]); w.writerows(geos)
with open(OUT/"DimProduct.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["ProductID","ProductCategory","Product","BaseUnitPriceINR","BaseUnitCostINR"]); w.writerows(products)
with open(OUT/"DimChannel.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["ChannelID","Channel","TypicalDiscount"]); w.writerows(channels)
with open(OUT/"DimSalesperson.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["SalespersonID","Salesperson","PrimaryRegion"]); w.writerows(salespeople)

customers=[]
for i in range(1500):
 g=random.choice(geos); customers.append((f"CUST{i+1:05d}",f"Customer {i+1:05d}",random.choice(segments),g[0],g[2],g[1]))
with open(OUT/"DimCustomer.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["CustomerID","CustomerName","CustomerSegment","GeographyID","Country","Region"]); w.writerows(customers)

dates=[]; d=date(2024,1,1)
while d<=date(2025,12,31):
 dates.append(d); d+=timedelta(days=1)
with open(OUT/"DimDate.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["Date","Year","Quarter","MonthNumber","Month","YearMonth","Weekday","IsWeekend"])
 for d in dates: w.writerow([d,d.year,f"Q{(d.month-1)//3+1}",d.month,d.strftime("%b"),d.strftime("%Y-%m"),d.strftime("%A"),int(d.weekday()>=5)])

month_factor={1:.92,2:.88,3:.92,4:.97,5:1,6:1.03,7:1.02,8:1.05,9:1.08,10:1.18,11:1.28,12:1.34}
region_factor={"APAC":1.08,"Europe":1.02,"North America":1.04,"MEA":.96,"Latin America":.91}
cust_by_geo={g[0]:[c for c in customers if c[3]==g[0]] for g in geos}
sp_by_region={r:[s for s in salespeople if s[2]==r] for r in regions}

with open(OUT/"FactSales.csv","w",newline="",encoding="utf-8") as f:
 w=csv.writer(f); w.writerow(["OrderID","OrderDate","CustomerID","GeographyID","ProductID","ChannelID","SalespersonID","Units","UnitPriceINR","DiscountPct","RevenueINR","CostINR","GrossProfitINR","TargetRevenueINR","Region","Country","ProductCategory","CustomerSegment","Channel"])
 for i in range(ROWS):
  d=random.choice(dates); g=random.choice(geos); p=random.choice(products); ch=random.choices(channels,weights=[31,34,23,12])[0]
  c=random.choice(cust_by_geo[g[0]]); sp=random.choice(sp_by_region[g[1]])
  units=max(1,int(np.random.gamma(2.2,7))); disc=max(0,min(.25,np.random.normal(ch[2],.025)))
  if d.month>=10 and random.random()<.22: disc=min(.25,disc+random.uniform(.02,.07))
  growth=1.075 if d.year==2025 else 1
  price=p[3]*random.uniform(.96,1.05); revenue=units*price*(1-disc)*growth*region_factor[g[1]]*month_factor[d.month]
  cost=units*p[4]*random.uniform(.98,1.05); gross=revenue-cost
  target=revenue*random.uniform(1.01,1.10)*(1.08 if g[1]=="Latin America" else 1)*(1.04 if ch[1]=="Online" else 1)
  w.writerow([f"ORD-{d.year}-{i+1:06d}",d,c[0],g[0],p[0],ch[0],sp[0],units,round(price,2),round(disc,4),round(revenue,2),round(cost,2),round(gross,2),round(target,2),g[1],g[2],p[1],c[2],ch[1]])

print(f"Generated {ROWS:,} synthetic transactions in {OUT.resolve()}")
