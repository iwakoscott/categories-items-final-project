from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Coffee, Origin, Base, User

engine = create_engine('sqlite:///coffeewithusers.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy origins

new_user_1 = User(name="Joe Latte",
                  email="joe.latte@cascara.com",
                  picture="https://goo.gl/yk3rjB")
session.add(new_user_1)
session.commit()

new_origin_2 = Origin(name='Brazil', user=new_user_1)
session.add(new_origin_2)
session.commit()

new_origin_3 = Origin(name='Burundi', user=new_user_1)
session.add(new_origin_3)
session.commit()

new_origin_8 = Origin(name='Costa Rica', user=new_user_1)
session.add(new_origin_8)
session.commit()

new_origin_13 = Origin(name='El Salvador', user=new_user_1)
session.add(new_origin_13)
session.commit()

new_origin_14 = Origin(name='Ethiopia', user=new_user_1)
session.add(new_origin_14)
session.commit()

new_user_2 = User(name="Sandy Mocha",
                  email="sandy_mocha@peets.com",
                  picture="https://goo.gl/MSYfr2")
session.add(new_user_2)
session.commit()

new_origin_17 = Origin(name='Guatemala', user=new_user_2)
session.add(new_origin_17)
session.commit()

new_origin_21 = Origin(name='India', user=new_user_2)
session.add(new_origin_21)
session.commit()

new_origin_25 = Origin(name='Kenya', user=new_user_2)
session.add(new_origin_25)
session.commit()

new_origin_30 = Origin(name='Mexico', user=new_user_2)
session.add(new_origin_30)
session.commit()

new_origin_31 = Origin(name='Nicaragua', user=new_user_2)
session.add(new_origin_31)
session.commit()

new_origin_33 = Origin(name='Panama', user=new_user_2)
session.add(new_origin_33)
session.commit()

new_origin_38 = Origin(name='Rwanda', user=new_user_2)
session.add(new_origin_38)
session.commit()

new_user_3 = User(name="Scott Espresso",
                  email="espresso_man@gmail.com",
                  picture="https://goo.gl/eUDRs8")
session.add(new_user_3)
session.commit()

new_origin_40 = Origin(name='Tanzania', user=new_user_3)
session.add(new_origin_40)
session.commit()

new_origin_42 = Origin(name='Timor Leste', user=new_user_3)
session.add(new_origin_42)
session.commit()

new_origin_45 = Origin(name='Uganda', user=new_user_3)
session.add(new_origin_45)
session.commit()

new_origin_49 = Origin(name='Zambia', user=new_user_3)
session.add(new_origin_49)
session.commit()

new_origin_50 = Origin(name='Zimbabwe', user=new_user_3)
session.add(new_origin_50)
session.commit()

# add coffees
coffee_0 = Coffee(name='Fazenda do Sertao Yellow Bourbon',
                  description='''Layered sugar and nut notes come off like
                  sweetened almond milk, and honey-glazed almond, and baker's
                  cocoa and hickory notes accent the finish. An approachable
                  Brazil favorable in middle to dark roasting. City+ to Full
                  City+. Good for espresso.''',
                  origin=new_origin_2,
                  user=new_user_1)

session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Santa Lucia Yellow Bourbon',
                  description='''Classic Brazil characteristics of big body,
                  low acidity, and balanced sweet to savory notes. Brown sugar,
                  almond paste, walnut, peanut cookie, cocoa powder, tamarind,
                  and leather. City+ to Vienna. Good for Espresso.''',
                  origin=new_origin_2,
                  user=new_user_1)
session.add(coffee_1)
session.commit()


coffee_0 = Coffee(name='Organic Santo Domingo La Cascada',
                  description='''This is a "coffee" coffee, a low-acid,
                  balanced cup. Understated fruit accents, core bittersweetness
                  of burnedcaramel, apple and cherimoya hints. City+ to Full
                  City+. Good for espresso.''',
                  origin=new_origin_30,
                  user=new_user_1)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Organic Tenejapa Kulaktik Coop',
                  description='''Winey flavors of grape and peach, rustic date
                  sugar, and a toasted coconut note are noted in City/C+
                  roasting, a mild black olive-like acidity, and walnut accent
                  note in the finish. City to Full City.''',
                  origin=new_origin_30,
                  user=new_user_1)
session.add(coffee_1)
session.commit()


coffee_0 = Coffee(name='Dry Process Los Angeles Bourbon',
                  description='''Intense fruit notes fill the cup in light and
                  dark roasts (even 2nd snaps!), dried strawberry and papaya,
                  fruit jam, raw sugar, and roasted almond and peanut aroma.
                  Big body, and very long finish. City to Full City+.''',
                  origin=new_origin_13,
                  user=new_user_1)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Finca Las Animas',
                  description='''A compact flavor profile, maple walnut, sugar
                  browning notes, and loads of bittersweet chocolate. Body,
                  balance, and sweet. Good as espresso. City+ to Full City+.
                  Good for espresso.''',
                  origin=new_origin_13,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Finca Santa Julia Bourbon',
                  description='''Santa Julia is sure to garner universal
                  acclaim, a real crowd pleaser. Raw sugar, roasted nut, and
                  cinnamon allude to granola, with hints of hazelnut, and dried
                  apple. City+ to Full City+. Good for espresso.''',
                  origin=new_origin_13,
                  user=new_user_2)
session.add(coffee_2)
session.commit()


coffee_0 = Coffee(name='Boquete Finca San Sebastian',
                  description='''Balance of sweet and bittering tones make this
                  a crowd favorite, dark caramel, red apple, toffee nut, black
                  tea, and crisp apple-like acidity. Roasted nut aroma. City+
                  to Full City.''',
                  origin=new_origin_33,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Volcan Baru Bambito',
                  description='''Crisp, sweet, balanced, and clean, Bambito is
                  versatile coffee, with flavors of marshmallow, brown sugar,
                  green tea, dried apple and walnut, and a finish that comes to
                  a point. City to Full City+. Good for espresso.''',
                  origin=new_origin_33,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_0 = Coffee(name='Ratnagiri Pearl Mountain Peaberry',
                  description='''Perhaps mild at first, Pearl Mountain Peaberry
                  intensifies greatly as it cools. A sweet aroma leads to
                  flavors of apple and grape, praline nut, stevia and lemon
                  balm herbs, and powdery cocoa. City to Full City.''',
                  origin=new_origin_21,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_0 = Coffee(name='Familia Bonillia',
                  description='''Honey wheat puff and cocoa aromatics, move
                  into flavors of cinnamon-dusted walnut, Jordan almonds,
                  bittersweet chocolate, and fruited hints. City+ to Full
                  City+. Good for espresso.''',
                  origin=new_origin_8,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Helsar Asdrubal Chavez',
                  description='''Asdrubal Chavez' coffee is restrained, sturdy,
                  and with balance of sweetness and bittering components:
                  toasted hazelnut, black tea, roasted malt, cacao, chocolate
                  sponge cake. Full City - Full City+. Good espresso.''',
                  origin=new_origin_8,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='La Casona -San Francisco 1900',
                  description='''San Francisco 1800 has focused milk chocolate
                  flavors, mild cinnamon stick and sugar browning notes,
                  and cacao nib aftertaste. Chocolate/hazelnut spread at Full
                  City. Full City to Full City+. SO Espresso.''',
                  origin=new_origin_8,
                  user=new_user_3)
session.add(coffee_2)
session.commit()


coffee_3 = Coffee(name='Tarrazu SWP Decaf',
                  description='''Impressive acidity, like white grape juice.
                  Liquid brown sugar, honey wheat bread, rice crispy treats,
                  and caramel popcorn. As espresso, you'd be hard pressed to
                  guess it's a decaf! Super versatile. City to Full City+.''',
                  origin=new_origin_8,
                  user=new_user_3)
session.add(coffee_3)
session.commit()


coffee_0 = Coffee(name='Lacao Village',
                  description='''Red raisin and honey wheat aromatics, baked
                  banana bread, roasted nut and grain notes, Yerba Mate tea.
                  Darker roasting brings out bittersweetness.''',
                  origin=new_origin_42,
                  user=new_user_3)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Organic Ermera Letefoho',
                  description='''Letefoho reminds me of a wet-processed Central
                  American coffee in many ways, raw sugar, honey-drizzled
                  walnut, apple, with rye and cocoa powder in the finish. City+
                  to Full City+.''',
                  origin=new_origin_42,
                  user=new_user_3)
session.add(coffee_1)
session.commit()


coffee_0 = Coffee(name='Agaro -Duromina Cooperative',
                  description='''2017 is a good year for Duromina, intense
                  flavors of peach and nectarine, and orange marmalade note is
                  attention grabbing. Deeper roasts pull out cacao
                  bittersweetness, dark berry, plum, and citrus rind. Moderate
                  acidity level. City to Full City. Good for espresso.''',
                  origin=new_origin_14,
                  user=new_user_3)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Agaro -Nano Challa Cooperative',
                  description='''Nano Challa is a structured cup, white honey
                  sweetness with mild fruit and jasmine floral accent notes,
                  ginger chews, citrus and Ricola-like dark herbal aspect. City
                  to Full City. Good for SO espresso or accent coffee for
                  espresso blending.''',
                  origin=new_origin_14,
                  user=new_user_3)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Dry Process Mormora Guji Highland',
                  description='''So complex on it's own, and a fantastic blend
                  component, this DP shows a wide range of fruit flavors:
                  melon, cooked rhubarb, strawberry milk, berry lambic, and
                  more. Great from City to Full City. Good espresso blend
                  component.''',
                  origin=new_origin_14,
                  user=new_user_3)
session.add(coffee_2)
session.commit()


coffee_3 = Coffee(name='Duromina SWP Decaf',
                  description='''As decaf, Duromina has much to celebrate.
                  Intense caramelized sugar sweetness, peach muffin, fleshy
                  fruit, lavender accent, and chocolate-covered wafer cookie.
                  City to Full City. Nice accent coffee for espresso.''',
                  origin=new_origin_14,
                  user=new_user_1)
session.add(coffee_3)
session.commit()


coffee_4 = Coffee(name='Kela Kochore Aseffa Station',
                  description='''Kela Kochore shows a delicate, shimmering
                  profile with a saturated red honey sweetness. Acidity is
                  bright, and accentuated by flavors of pomelo, sweet lime,
                  and mandarin orange. Overt florals add to this dynamic cup.
                  City to Full City.''',
                  origin=new_origin_14,
                  user=new_user_1)
session.add(coffee_4)
session.commit()


coffee_5 = Coffee(name='Shakiso Mormora Farm',
                  description='''Mormora is a beautiful cup, "refreshing" in a
                  way. Earl Grey with bergamot oil, rose water florals,
                  citrus oil, and acidity that's like sweet tea with lemon
                  spritz. Best at City to City+ roast level.''',
                  origin=new_origin_14,
                  user=new_user_1)
session.add(coffee_5)
session.commit()


coffee_0 = Coffee(name='Acatenango Gesha Lot 2',
                  description='''A stellar Gesha coffee, perfumed florals,
                  jasmine and orange blossom, and honeyed sweetness. Tropical
                  fruits, herbal and black teas, cinnamon sticks, and brilliant
                  acidity. "Gesha" characteristics all the way. City to
                  City+.''',
                  origin=new_origin_17,
                  user=new_user_1)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Antigua Pulcal Inteligente Lot 1',
                  description='''Turbinado sugar to almond past sweetness,
                  apple like acidity, delicate pear note, black tea with lemon,
                  orange rind, and high % cacao. A superb brewed coffee across
                  the roast spectrum. City to Full City+. Good for
                  espresso.''',
                  origin=new_origin_17,
                  user=new_user_1)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Cuilco Finca El Regalito',
                  description='''Regalito is on the level of a
                  competition-winning Guatemala. Raw sugar and floral honey
                  sweetness, dried pineapple, golden raisin, chamomile tea,
                  with elegant tea-like acidity, and Darjeeling tea in the long
                  aftertaste. City to Full City. Good for espresso.''',
                  origin=new_origin_17,
                  user=new_user_1)
session.add(coffee_2)
session.commit()


coffee_3 = Coffee(name='Huehuetenango Finca Rosma Lot 1',
                  description='''Rosma's acidity pops like fruit juice in light
                  to mid roasts, notes of honey, five spice, apple, dried plum,
                  Earl Grey. Big body and finishes so sweet. City to Full
                  City+. Good for espresso.''',
                  origin=new_origin_17,
                  user=new_user_1)
session.add(coffee_3)
session.commit()


coffee_4 = Coffee(name='Pico Mayor Gesha',
                  description='''This late 2016 harvest arrival has a mix of
                  root and herbal tones, fruited florals, notes of tamarind
                  paste, dried papaya, and a smokey cedar flavor that reminds
                  me of bbq pineapple. Like a cross between a rustic-toned
                  washed Sumatra and floral Gesha types. City+ to Full City.
                  Delicious espresso.''',
                  origin=new_origin_17,
                  user=new_user_1)
session.add(coffee_4)
session.commit()


coffee_5 = Coffee(name='Xinabajul Producers',
                  description='''Caramel sugar sweetness, cocoa powder-dusted
                  almonds, and crisp apple accent. A balanced coffee with
                  tea-like brightness. Cocoa flavors build with roast, and
                  Full City and beyond are true dual-use. City+ to Full City+.
                  Good for espresso.''',
                  origin=new_origin_17,
                  user=new_user_1)
session.add(coffee_5)
session.commit()


coffee_0 = Coffee(name='Kivu Kageyo Station Lot 1',
                  description='''Kageyo is complex in light to middle roasts,
                  cinnamon tea, sugarcane juice, vanilla bean, and red apple.
                  Our City+ roast showed pomelo-like acidity, dark berry,
                  cream soda, and baking spice. City to Full City. Good for
                  espresso.''',
                  origin=new_origin_38,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Nyamasheke Nyungwe Cooperative',
                  description='''Compact brown sugar sweetness at City+ roast,
                  with Earl Grey tea, 5 spice accent, and an interesting fruit
                  flavor that reminded me of Dr. Pepper. City+ to Full City.
                  Good for espresso.''',
                  origin=new_origin_38,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Rulindo -Tumba Station',
                  description='''Tumba is a complex Rwandan coffee, clear
                  sweetness, layered fruit, and citric acidity. Middle roasts
                  show lemony Assam tea, golden raisin, cherry hard candies,
                  tamarind chew, and simple syrup sweetness. City to Full City.
                  Good espresso at FC.''',
                  origin=new_origin_38,
                  user=new_user_2)
session.add(coffee_2)
session.commit()


coffee_3 = Coffee(name='Rulindo Cocatu Cooperative Lot 3',
                  description='''Always a shining star, Cocatu has a Medjool
                  date aroma, brown sugar sweetness in the cup, with accents of
                  chamomile flower tea, cinnamon sauce, clove, and fig pudding.
                  Deeper roast levels produce incredible level of dark
                  chocolate. City+ to Full City+. Good for espresso.''',
                  origin=new_origin_38,
                  user=new_user_2)
session.add(coffee_3)
session.commit()


coffee_4 = Coffee(name='Rulindo Cooperatives SWP Decaf',
                  description='''A balanced decaf at City+/Full City roasts,
                  powdery baker's cocoa bittering tones balanced by flavor of
                  raw sugar and cinnamon, offset by savory accents, and a
                  creamy Macadamia nut note. City+ to Full City.
                  Good for espresso.''',
                  origin=new_origin_38,
                  user=new_user_2)
session.add(coffee_4)
session.commit()


coffee_0 = Coffee(name='Cheema Kapchorwa',
                  description='''Heavily laden with layers of rich chocolate
                  flavors, with dark stone fruits laying just beneath the
                  surface. Minimally processed sugars balance cacao flavors,
                  and body is extremely viscous. Full City to Full City+.
                  Good for espresso.''',
                  origin=new_origin_45,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Mount Elgon Sipi Falls',
                  description='''A unique Ugandan cup, grabby lemon citrus,
                  barley tea and green apple top notes, a base bittersweetness
                  of sucanat, rice syrup, and baker's cocoa. Finishes with
                  cedar aroma. City+ to Full City.''',
                  origin=new_origin_45,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_0 = Coffee(name='Kayanza Dusangirijambo Coop',
                  description='''City+ is a near perfect cup, dark currant,
                  Lipton black tea, simple syrup, cocoa powder hints, and
                  lemonade-like brightness. Ideal for light roasting. City
                  to City+.''',
                  origin=new_origin_3,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Kayanza SWP Decaf',
                  description='''One of the best decafs from this latest bunch,
                  Burundi Kayanza SWP shows balanced bittersweetness,
                  cheap dark chocolate, unsweetened baking cocoa, a dusting of
                  cinnamon spice, subtle raisin and barley malt hits. City+ to
                  Full City+. Excels as espresso.''',
                  origin=new_origin_3,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Kazosa N\'Ikawa Station',
                  description='''Incredible brewed, flavors of cherry,
                  clove spice, sugarcane juice, marzipan, and a tart-sweet
                  lemonade brightness highlight this Burundi cup. Such a
                  refined cup profile with pointed finish. City to City+.''',
                  origin=new_origin_3,
                  user=new_user_2)
session.add(coffee_2)
session.commit()


coffee_3 = Coffee(name='Kibumbu Kayokwe Lot 1',
                  description='''Kayokwe is wonderful brewed in lighter roast
                  shades, tea-like to lemon brightness, dark cranberry juice,
                  complex baking spice notes, and resonant sweetness.
                  A sparkling cup. City to City+.''',
                  origin=new_origin_3,
                  user=new_user_2)
session.add(coffee_3)
session.commit()


coffee_4 = Coffee(name='Rubanda Station',
                  description='''Cane juice sweetness, with notes of dried
                  cherry, orange tea, graham cracker, and a tart lemon accent.
                  Floral and raspberry leaf hints mark the finish. Big body in
                  the darker roast levels. City to Full City+.
                  Great for espresso.''',
                  origin=new_origin_3,
                  user=new_user_2)
session.add(coffee_4)
session.commit()


coffee_0 = Coffee(name='Kirinyaga Gakuyu-ini AB',
                  description='''Gakuyu-ini is complex, has layered sweetness,
                  and downright tropical in the light roasts. Citrus notes go
                  from fresh squeezed orange to the pithy/bittering aspects of
                  the peel itself. Great option for dark roasting too with
                  substantial bittersweetness. City+ to Full City+.
                  Wild espresso.''',
                  origin=new_origin_25,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Muranga Riakiberu AA',
                  description='''A bright cup, especially at moderate
                  temparatures. From start to finish, the sweetness goes from
                  sugarcane juice, to barley malt and rice syrup. Top notes
                  include cantelope, lemon-rhubarb, celery soda, and fruit tea.
                  City+ to Full City.''',
                  origin=new_origin_25,
                  user=new_user_2)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Muranga Riakiberu AB',
                  description='''Complex flavor matrix, transparent simple
                  syrup sweetness, tart lemon-lime, cranberry sauce, concord
                  grape juice, and orange zest, and a grabby citric acidity.
                  Great at a fairly wide roast range. City to Full City.''',
                  origin=new_origin_25,
                  user=new_user_2)
session.add(coffee_2)
session.commit()


coffee_3 = Coffee(name='Nyeri Gathaithi AB',
                  description='''One of the best AB's of the year for us,
                  acidity that comes off like lemon spritzed herbal tea,
                  flavors of melon, apple, fresh mint, coconut water, sugarcane
                  juice, shaved lemon. City to Full City.''',
                  origin=new_origin_25,
                  user=new_user_2)
session.add(coffee_3)
session.commit()


coffee_0 = Coffee(name='Acopio Suyatal',
                  description='''Suyatal has understated, yet persistent
                  sweetness all the way up to 2nd snaps. Bittering cocoa and
                  raw sugars find near perfect balance, with citrus rind, and
                  toasted nut. City+ to Full City+. Good for espresso.''',
                  origin=new_origin_31,
                  user=new_user_2)
session.add(coffee_0)
session.commit()


coffee_1 = Coffee(name='Buenos Aires Maracaturra Lot 1',
                  description='''City to City+ roasts yield balanced caramel
                  and roasted almond core flavors, topped off with accents of
                  honey, chamomile florals, dried apple and apricot, cilantro,
                  and tea-like brightness. City to City+.''',
                  origin=new_origin_31,
                  user=new_user_1)
session.add(coffee_1)
session.commit()


coffee_2 = Coffee(name='Finca Buenos Aires Caturra',
                  description='''Raw sugar and vanilla, roasted almond, and a
                  dusting of milk chocolate to bittersweet cacao powder.
                  Crowd-pleasing, balanced, bodied, low-acid cup that works
                  well as dual-use. City+ to Full City+. Good for espresso.''',
                  origin=new_origin_31,
                  user=new_user_1)
session.add(coffee_2)
session.commit()


coffee_0 = Coffee(name='Mbeya Iyula AB',
                  description='''Iyula has a clear, cane sugar sweetness, with
                  fruit to herbal accents, dark cranberry, licorice, and blood
                  orange. Body is oily, and acidity grabby, like orange pulp.
                  City+ to Full City+. Good for espresso.''',
                  origin=new_origin_40,
                  user=new_user_1)
session.add(coffee_0)
session.commit()


coffee_0 = Coffee(name='Kasama Estates',
                  description='''The profile boasts pungent molasses, pipe
                  tobacco leaves, rustic earth tones, and cooked rhubarb.
                  Impressive body carries bittersweetness long in the
                  aftertaste. City+ to Vienna''',
                  origin=new_origin_49,
                  user=new_user_1)
session.add(coffee_0)
session.commit()

print "coffee added!"
