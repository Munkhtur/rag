import markdownify

html = """
<div id="branch-listing-container">
					<div class="branch-listing" style="height: 357px;">
			<a class="branch-card" id="branch-262626" href="/branches/262626">
	<h5 class="card-title">Токио дахь Төлөөлөгчийн газар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/262626.jpg" class="card-img-top" alt="Токио дахь Төлөөлөгчийн газар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Токио дахь Төлөөлөгчийн газар Токио хот Чиёода дүүрэг Марүно-үчи 1-4-1 Эйракү барилга 23 давхар</p></div></div></a>

			<a class="branch-card" id="branch-421" href="/branches/421">
	<h5 class="card-title">Баянцээл салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/421.jpg" class="card-img-top" alt="Баянцээл салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70008978 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70008979 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 15-р хороолол, 7-р хороо, Их тойруу 24/1</p></div></div></a>

			<a class="branch-card" id="branch-423" href="/branches/423">
	<h5 class="card-title">Нарны зам салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/423.jpg" class="card-img-top" alt="Нарны зам салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 452874 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	452873 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 13-р хороолол, 18-р хороо, Манлайбаатар Дамдинсvрэнгийн гудамж, "Diamond" оффис, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-426" href="/branches/426">
	<h5 class="card-title">Баянзүрх салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/426.jpg" class="card-img-top" alt="Баянзүрх салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70008971 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70008972 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Энхтайваны өргөн чөлөө, Б/59 байр</p></div></div></a>

			<a class="branch-card" id="branch-434" href="/branches/434">
	<h5 class="card-title">Тэнгэр Плаза салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/434.jpg" class="card-img-top" alt="Тэнгэр Плаза салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70114343 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70114344 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 8-р хороо, офицеруудын ордноос уруудаад, Тэнгэр плаза худалдааны төвийн 2-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-435" href="/branches/435">
	<h5 class="card-title">Дүнжингарав салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/435.jpg" class="card-img-top" alt="Дүнжингарав салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77070435 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	77000435 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 26-р хороо, Нийслэл хүрээ өргөн чөлөө гудамж, Дүнжингарав худалдааны төвийн урд, 603-р байр, 2 давхар</p></div></div></a>

			<a class="branch-card" id="branch-438" href="/branches/438">
	<h5 class="card-title">Нарантуул салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/438.jpg" class="card-img-top" alt="Нарантуул салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					10:00-18:00
				<br>
								<strong>Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям:</strong>
					Амарна
				<br>
								<strong>Ням:</strong>
					10:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70004078 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70003078 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Нарантуул ОУХТ, Баялаг Ундраа худалдааны төвийн 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-441" href="/branches/441">
	<h5 class="card-title">Парк-Од салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/441.jpg" class="card-img-top" alt="Парк-Од салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77017474 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	77018484 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 26-р хороо Парк-Од худалдааны төв 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-447" href="/branches/447">
	<h5 class="card-title">Улаанхуаран тооцооны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/447.jpg" class="card-img-top" alt="Улаанхуаран тооцооны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					09:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75050617
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75050616<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянзүрх дүүрэг, 40-р хороо, Улаанхуаран, Кайду моол 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-450" href="/branches/450">
	<h5 class="card-title">Торгон хил салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/450.jpg" class="card-img-top" alt="Торгон хил салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77001655 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	77001644 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 2-р хороо, Ундрам Плаза, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-457" href="/branches/457">
	<h5 class="card-title">Сансар салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/457.jpg" class="card-img-top" alt="Сансар салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 453525&nbsp;/Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	450216 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 15-р хороо, Энхтайваны єргєн чєлєє-39</p></div></div></a>

			<a class="branch-card" id="branch-459" href="/branches/459">
	<h5 class="card-title">Сандэй плаза лайт хэсэг</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/459.jpg" class="card-img-top" alt="Сандэй плаза лайт хэсэг">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:45
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75050610 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75050620  /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Намьяанжугийн гудамж-37, Sunday плазагийн байр</p></div></div></a>

			<a class="branch-card" id="branch-809" href="/branches/809">
	<h5 class="card-title">Жуков салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/809.jpg" class="card-img-top" alt="Жуков салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(11) 450715 /Зээлийн мэргэжилтэн/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70000715  /Мэдээллийн ажилтан/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 4-р хороо, Энхтайван 46а гудамж, “Норжин” худалдааны төвийн 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-81102" href="/branches/81102">
	<h5 class="card-title">ШУТИС-БУХС ТООЦООНЫ КАСС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/81102.jpg" class="card-img-top" alt="ШУТИС-БУХС ТООЦООНЫ КАСС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			.
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 2-р хороо, ШУТИС-БУХС-ийн хичээлийн 5-р байр, 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-81801" href="/branches/81801">
	<h5 class="card-title">ДҮНЖИНГАРАВ ТООЦООНЫ КАСС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/81801.jpg" class="card-img-top" alt="ДҮНЖИНГАРАВ ТООЦООНЫ КАСС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					07:00-16:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			318553
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 26-р хороо, Дүнжингарав худалдааны төв, Нийслэлийн нэг цэгийн үйлчилгээний төв</p></div></div></a>

			<a class="branch-card" id="branch-5" href="/branches/5">
	<h5 class="card-title">НАТУР ТРЭЙД ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5.jpg" class="card-img-top" alt="НАТУР ТРЭЙД ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Натур худалдааны төв дотор В1 давхарын зүүн талд</p></div></div></a>

			<a class="branch-card" id="branch-7" href="/branches/7">
	<h5 class="card-title">НОМИН ЖУКОВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/7.jpg" class="card-img-top" alt="НОМИН ЖУКОВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:30-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Энхтайвны өргөн чөлөө, 14-р хороо, Төв замын урд, Номин супертакетруу ороод үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-17" href="/branches/17">
	<h5 class="card-title">АМГАЛАН САНСАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/17.jpg" class="card-img-top" alt="АМГАЛАН САНСАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Тэнгэр плаза төвийн замын эсрэг талд Амгалан сансар төв дотор 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-20" href="/branches/20">
	<h5 class="card-title">НОМИН ОЛЛМАРТ 13</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/20.jpg" class="card-img-top" alt="НОМИН ОЛЛМАРТ 13">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Бям:</strong>
					09:00-20:30
				<br>
								<strong>Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14-р хороо, Халвдарт, Номин оллмарт үйлчилгээний төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-22" href="/branches/22">
	<h5 class="card-title">САНСАР ТУНЕЛЬ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/22.jpg" class="card-img-top" alt="САНСАР ТУНЕЛЬ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
18-р хороо, 13-р хороолол, сансарын туннел дээрх Сансар худалдааны төвийн 1 давхар  </p></div></div></a>

			<a class="branch-card" id="branch-39" href="/branches/39">
	<h5 class="card-title">ФРЕСКО БАЯНМОНГОЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/39.jpg" class="card-img-top" alt="ФРЕСКО БАЯНМОНГОЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 12-р хороо, Баянмонгол хороолол дотор Fresco супермаркет дотор</p></div></div></a>

			<a class="branch-card" id="branch-49" href="/branches/49">
	<h5 class="card-title">МИНИЙ ХАЙПЕРМАРКЕТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/49.jpg" class="card-img-top" alt="МИНИЙ ХАЙПЕРМАРКЕТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 6-р хороо, Нарны зам дагуу, Миний хайпермаркетын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-50" href="/branches/50">
	<h5 class="card-title">МИНИЙ ДЭЛГҮҮР ЗҮҮН 4 ЗАМ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/50.jpg" class="card-img-top" alt="МИНИЙ ДЭЛГҮҮР ЗҮҮН 4 ЗАМ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, Зүүн 4 замын миний дэлгүүр, 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-86" href="/branches/86">
	<h5 class="card-title">ЖУКОВ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/86.jpg" class="card-img-top" alt="ЖУКОВ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
4-р хороо, Энхтайван 46а гудамж, “Норжин” худалдааны төвийн 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-93" href="/branches/93">
	<h5 class="card-title">ЭКО МАРКЕТ 13</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/93.jpg" class="card-img-top" alt="ЭКО МАРКЕТ 13">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Мяг:</strong>
					09:00-20:00
				<br>
								<strong>Лха:</strong>
					Амарна
				<br>
								<strong>Пүр-Баа:</strong>
					09:00-20:00
				<br>
								<strong>Бям-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД 25-р хороо, Сандэй худалдааны төвийн хажууд, Улаанбаатар их сургуулийн хашаан дотор, ЭКО худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-109" href="/branches/109">
	<h5 class="card-title">БАЯНЗҮРХ ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/109.jpg" class="card-img-top" alt="БАЯНЗҮРХ ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					10:00-16:00
				<br>
								<strong>Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Баа:</strong>
					10:00-16:00
				<br>
								<strong>Бям:</strong>
					Амарна
				<br>
								<strong>Ням:</strong>
					10:00-16:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянзүрх хүнс барааны захын баруун хойд хаалган дээр 
</p></div></div></a>

			<a class="branch-card" id="branch-113" href="/branches/113">
	<h5 class="card-title">НАРНЫ ЗАМ САЛБАР 1</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/113.jpg" class="card-img-top" alt="НАРНЫ ЗАМ САЛБАР 1">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14-р хороо, Намьяанжугийн гудамж-37, Sunday плазагийн үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-117" href="/branches/117">
	<h5 class="card-title">ДА ХҮРЭЭ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/117.jpg" class="card-img-top" alt="ДА ХҮРЭЭ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, Шархадны замд, Да-Хүрээ техникийн захын байр, Манду хаусын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-126" href="/branches/126">
	<h5 class="card-title">АТМ 2-Р ЭМНЭЛЭГ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/126.jpg" class="card-img-top" alt="АТМ 2-Р ЭМНЭЛЭГ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 3-р хороо, Бөхийн Өргөөний замын эсрэг талд Улсын 2-р төв эмнэлэгийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-127" href="/branches/127">
	<h5 class="card-title">И-МАРТ ЧИНГИС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/127.jpg" class="card-img-top" alt="И-МАРТ ЧИНГИС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-19:30
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Чингис зочид буудал, E-Mart супермаркет</p></div></div></a>

			<a class="branch-card" id="branch-142" href="/branches/142">
	<h5 class="card-title">КОМБИНИ ДАРЬ ЭХ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/142.jpg" class="card-img-top" alt="КОМБИНИ ДАРЬ ЭХ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 21-р хороо, Сэлбэ 26-618, Дарь эхээс 17 явах замд,  Миний дэлгүүр дотор</p></div></div></a>

			<a class="branch-card" id="branch-153" href="/branches/153">
	<h5 class="card-title">ОФИЦЕР ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/153.jpg" class="card-img-top" alt="ОФИЦЕР ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, Офицер захын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-162" href="/branches/162">
	<h5 class="card-title">НОМИН СКАЙ ТАУН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/162.jpg" class="card-img-top" alt="НОМИН СКАЙ ТАУН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Бям:</strong>
					09:00-20:30
				<br>
								<strong>Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 13-р хороо, Кино үйлдвэрийн зам урд, СКАЙ ТАУН-1 НОМИН, 2 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-168" href="/branches/168">
	<h5 class="card-title">БАЯЛАГ УНДРАА ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/168.jpg" class="card-img-top" alt="БАЯЛАГ УНДРАА ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Ням:</strong>
					11:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Нарантуул ОУХТ, "Баялаг Ундраа" худалдааны төвийн 1 давхарт зүүн хойд хаалган дээр </p></div></div></a>

			<a class="branch-card" id="branch-172" href="/branches/172">
	<h5 class="card-title">СОМАНГ ПЛАЗА </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/172.jpg" class="card-img-top" alt="СОМАНГ ПЛАЗА ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					07:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
13-р хорооллын автобусны буудлын хажууд байрлах Соманг плаза-н 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-173" href="/branches/173">
	<h5 class="card-title">Эко зах - Улаанхуаран</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/173.jpg" class="card-img-top" alt="Эко зах - Улаанхуаран">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 16-р хороо, Эко хүнсний захын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-178" href="/branches/178">
	<h5 class="card-title">НОМИН ЗҮҮН 4 ЗАМ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/178.jpg" class="card-img-top" alt="НОМИН ЗҮҮН 4 ЗАМ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Бям:</strong>
					09:00-20:30
				<br>
								<strong>Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Американ дэнж, Гялс төв рүү өгсөх зам дагуу Номингийн 2 давхар</p></div></div></a>

			<a class="branch-card" id="branch-184" href="/branches/184">
	<h5 class="card-title">ЧАНДМАНЬ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/184.jpg" class="card-img-top" alt="ЧАНДМАНЬ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Халдвартын Аман хуур хотхоны эсрэг талд, Чандмань төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-186" href="/branches/186">
	<h5 class="card-title">ДАРЬ ЭХ ЗАХ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/186.jpg" class="card-img-top" alt="ДАРЬ ЭХ ЗАХ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 27-р хороо, Сэлбэ-8, Дарь эх захын 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-187" href="/branches/187">
	<h5 class="card-title">ВЭЛЛМАРТ БОТАНИК</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/187.jpg" class="card-img-top" alt="ВЭЛЛМАРТ БОТАНИК">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 12-р хороо Ботаникийн эцэс, Wellmart-н 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-188" href="/branches/188">
	<h5 class="card-title">Буянт ухаа хороолол 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/188.jpg" class="card-img-top" alt="Буянт ухаа хороолол 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-21:00
				<br>
								<strong>Бям:</strong>
					10:00-20:00
				<br>
								<strong>Ням:</strong>
					10:30-19:30
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 15-р хороо Буянт ухаа 2 хороололлын, Хонгор худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-194" href="/branches/194">
	<h5 class="card-title">Дүнжингарав салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/194.jpg" class="card-img-top" alt="Дүнжингарав салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 26-р хороо, Нийслэл хүрээ өргөн чөлөө гудамж, Дүнжингарав худалдааны төвийн урд, Чухаг хотхоны 603-р байр, 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-206" href="/branches/206">
	<h5 class="card-title">ГЭР БҮЛ ХУДАЛДААНЫ ТӨВ ЧУЛУУН ОВОО</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/206.jpg" class="card-img-top" alt="ГЭР БҮЛ ХУДАЛДААНЫ ТӨВ ЧУЛУУН ОВОО">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-22:00
				<br>
								<strong>Бям-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Чулуун овоо Гэр бүл худалдааны төв</p></div></div></a>

			<a class="branch-card" id="branch-208" href="/branches/208">
	<h5 class="card-title">ЭКО МАРКЕТ ЖУКОВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/208.jpg" class="card-img-top" alt="ЭКО МАРКЕТ ЖУКОВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-22:00
				<br>
								<strong>Бям-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Жуков худалдааны төвийн хажууд</p></div></div></a>

			<a class="branch-card" id="branch-211" href="/branches/211">
	<h5 class="card-title">САРУУЛ МАРКЕТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/211.jpg" class="card-img-top" alt="САРУУЛ МАРКЕТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД 6-р хороо,  Сэлбэ голын төмөр гүүр даваад Саруул маркет
</p></div></div></a>

			<a class="branch-card" id="branch-214" href="/branches/214">
	<h5 class="card-title">ЭФЭС БӨХИЙН ӨРГӨӨ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/214.jpg" class="card-img-top" alt="ЭФЭС БӨХИЙН ӨРГӨӨ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Бөхийн өргөөгийн ард хуучнаар Шинэ сонголт дэлгүүрийн байранд, Эфэс худалдааны төв дотор
</p></div></div></a>

			<a class="branch-card" id="branch-230" href="/branches/230">
	<h5 class="card-title">АТМ БЗД ТАТВАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/230.jpg" class="card-img-top" alt="АТМ БЗД ТАТВАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 13-р хороо, БЗДТатварын хэлтэс
</p></div></div></a>

			<a class="branch-card" id="branch-95800061" href="/branches/95800061">
	<h5 class="card-title">LPG GRAND SPA ( Discount 2% , 2% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800061.jpg" class="card-img-top" alt="LPG GRAND SPA ( Discount 2% , 2% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11450202
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянзүрх дүүрэг, 1-р хороо, 8, 8-р байр, 3-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-95800066" href="/branches/95800066">
	<h5 class="card-title">MARC SHOP ( Discount 3% , 6% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800066.jpg" class="card-img-top" alt="MARC SHOP ( Discount 3% , 6% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			98115909
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Их хүрээ гудамж</p></div></div></a>

			<a class="branch-card" id="branch-95800070" href="/branches/95800070">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800070.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗДүүргийн эмнэлэг</p></div></div></a>

			<a class="branch-card" id="branch-95800071" href="/branches/95800071">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800071.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Саруул тэнгэр хотхон</p></div></div></a>

			<a class="branch-card" id="branch-95800072" href="/branches/95800072">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800072.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Халдварт автобусны буудал</p></div></div></a>

			<a class="branch-card" id="branch-95800074" href="/branches/95800074">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800074.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Хавдар судлал</p></div></div></a>

			<a class="branch-card" id="branch-95800080" href="/branches/95800080">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800080.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Encanto</p></div></div></a>

			<a class="branch-card" id="branch-95800081" href="/branches/95800081">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800081.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Амгалан зах</p></div></div></a>

			<a class="branch-card" id="branch-95800082" href="/branches/95800082">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800082.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Оргил төв</p></div></div></a>

			<a class="branch-card" id="branch-95800083" href="/branches/95800083">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800083.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Баянмонгол хороолол</p></div></div></a>

			<a class="branch-card" id="branch-95800088" href="/branches/95800088">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800088.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Монос Баянцээл</p></div></div></a>

			<a class="branch-card" id="branch-95800092" href="/branches/95800092">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800092.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД 2-р эмнэлэг</p></div></div></a>

			<a class="branch-card" id="branch-95800095" href="/branches/95800095">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800095.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Жуков</p></div></div></a>

			<a class="branch-card" id="branch-95800096" href="/branches/95800096">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800096.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, Баянзүрх зах</p></div></div></a>

			<a class="branch-card" id="branch-95800098" href="/branches/95800098">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800098.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Хорго хотхон</p></div></div></a>

			<a class="branch-card" id="branch-95800102" href="/branches/95800102">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800102.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Чингис зочид буудал</p></div></div></a>

			<a class="branch-card" id="branch-95800105" href="/branches/95800105">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800105.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД EMART</p></div></div></a>

			<a class="branch-card" id="branch-95800106" href="/branches/95800106">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800106.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Home Plaza 2</p></div></div></a>

			<a class="branch-card" id="branch-95800125" href="/branches/95800125">
	<h5 class="card-title">ШҮР САЛОН ( Discount 5% , 8% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800125.jpg" class="card-img-top" alt="ШҮР САЛОН ( Discount 5% , 8% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70377300
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД Сансар</p></div></div></a>

			<a class="branch-card" id="branch-43" href="/branches/43">
	<h5 class="card-title">УНДРАМ ПЛАЗА </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/43.jpg" class="card-img-top" alt="УНДРАМ ПЛАЗА ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 2-р хороо, Торгон хил садбарын үүдэнд, сансарын колонк, Ундрам плаза 1-р давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-69" href="/branches/69">
	<h5 class="card-title">ШИНЭ САНСАР ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/69.jpg" class="card-img-top" alt="ШИНЭ САНСАР ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
3-р хороо, КТМС замын эсрэг талд колонкын урд, Шинэ сансар захын 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-76" href="/branches/76">
	<h5 class="card-title">БАЯНЗҮРХ ХУДАЛДААНЫ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/76.jpg" class="card-img-top" alt="БАЯНЗҮРХ ХУДАЛДААНЫ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 16-р хороо, 16-р хороолол, Баянзүрх худалдааны төвийн 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-85" href="/branches/85">
	<h5 class="card-title">БАЯНЦЭЭЛ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/85.jpg" class="card-img-top" alt="БАЯНЦЭЭЛ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
15-р хороолол, 7-р хороо, Их тойруу 24/1, Баянцээл салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-114" href="/branches/114">
	<h5 class="card-title">НАРНЫ ЗАМ САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/114.jpg" class="card-img-top" alt="НАРНЫ ЗАМ САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14-р хороо, Намьяанжугийн гудамж-37, Sunday плазагийн үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-133" href="/branches/133">
	<h5 class="card-title">ДҮНЖИНГАРАВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/133.jpg" class="card-img-top" alt="ДҮНЖИНГАРАВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, Дүнжингарав худалдааны төвийн 1 давхарт, баруун хойд буланд 
</p></div></div></a>

			<a class="branch-card" id="branch-144" href="/branches/144">
	<h5 class="card-title">АМГАЛАН ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/144.jpg" class="card-img-top" alt="АМГАЛАН ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, Амгалан захын 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-155" href="/branches/155">
	<h5 class="card-title">ТЭНГЭР ПЛАЗА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/155.jpg" class="card-img-top" alt="ТЭНГЭР ПЛАЗА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 8 хороо, Тэнгэр Плаза, 2 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-174" href="/branches/174">
	<h5 class="card-title">БАЯНЗҮРХ САЛБАР ӨРГӨТГӨЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/174.jpg" class="card-img-top" alt="БАЯНЗҮРХ САЛБАР ӨРГӨТГӨЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14-р хороо, Энхтайваны єргєн чєлєє Б/59 байр, Зүүн хүрээ хотхоны цаана, Баянзүрх салбар дотор
</p></div></div></a>

			<a class="branch-card" id="branch-177" href="/branches/177">
	<h5 class="card-title">НАРНЫ ЗАМ САЛБАР 3</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/177.jpg" class="card-img-top" alt="НАРНЫ ЗАМ САЛБАР 3">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сандэй плазагийн 4 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-189" href="/branches/189">
	<h5 class="card-title">GS25 БАЯНЗҮРХ ЗАХ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/189.jpg" class="card-img-top" alt="GS25 БАЯНЗҮРХ ЗАХ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
УБ хот, БЗД, 6-р хороо, Энхтайваны өргөн чөлөө, Баянзүрх зах GS25 </p></div></div></a>

			<a class="branch-card" id="branch-198" href="/branches/198">
	<h5 class="card-title">НАРАНТУУЛ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/198.jpg" class="card-img-top" alt="НАРАНТУУЛ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14-р хороо, Нарантуул ОУХТ, Баялаг Ундраа худалдааны төвийн 1 давхарт, Салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-199" href="/branches/199">
	<h5 class="card-title">НАРНЫ ЗАМ ДАЙМОНД</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/199.jpg" class="card-img-top" alt="НАРНЫ ЗАМ ДАЙМОНД">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 13-р хороолол, 18-р хороо, Манлайбаатар Дамдинсvрэнгийн гудамж, "Diamond" оффис</p></div></div></a>

			<a class="branch-card" id="branch-229" href="/branches/229">
	<h5 class="card-title">ЖИ ЭС 25 ТОД </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/229.jpg" class="card-img-top" alt="ЖИ ЭС 25 ТОД ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Халдвартын эцсийн буудал Тод төв, GS25 дотор
</p></div></div></a>

			<a class="branch-card" id="branch-404" href="/branches/404">
	<h5 class="card-title">Энхтайван салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/404.jpg" class="card-img-top" alt="Энхтайван салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			312679 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	318982 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Энхтайваны өргөн чөлөө 17-д байрлах "Блю Скай Тауэр" барилгын 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-409" href="/branches/409">
	<h5 class="card-title">Сөүл салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/409.jpg" class="card-img-top" alt="Сөүл салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			331319 /Мэдээллийн ажилтан/ &lt;br&gt;
331318
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	40902 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Сөүл гудамж, 33-р байр, Хэрлэн Плаза 2-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-410" href="/branches/410">
	<h5 class="card-title">Гурван гал салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/410.jpg" class="card-img-top" alt="Гурван гал салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			318765 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	310386 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, "МОННИС" цамхаг, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-417" href="/branches/417">
	<h5 class="card-title">Дөчин мянгат салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/417.jpg" class="card-img-top" alt="Дөчин мянгат салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-20:00
				<br>
								<strong>Бям-Ням:</strong>
					10:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7012 7094
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7012 7096 /Мэдээллийн ажилтан/ &lt;br&gt;
7012 7095 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 4-р хороо, Сєvлийн гудамж, хуучнаар Хүнсний 50-р дэлгүүр, 2 давхар</p></div></div></a>

			<a class="branch-card" id="branch-425" href="/branches/425">
	<h5 class="card-title">Их наяд Лайт хэсэг</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/425.jpg" class="card-img-top" alt="Их наяд Лайт хэсэг">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:45
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75056644 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75056633 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Хаяг: СБД, 1-р хороо, Их монгол улсын гудамж-04, Их наяд худалдааны төвийн 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-428" href="/branches/428">
	<h5 class="card-title">Пийс тауэр салбарын өргөтгөл</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/428.jpg" class="card-img-top" alt="Пийс тауэр салбарын өргөтгөл">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Ням:</strong>
					10:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7000-6994 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7000-6993 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Энхтайваны єргєн чєлєє-57, Улаанбаатар Их Дэлгvvр, B1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-432" href="/branches/432">
	<h5 class="card-title">Шангри-Ла Салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/432.jpg" class="card-img-top" alt="Шангри-Ла Салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70000256 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70000257 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Олимпийн гудамж - 19, “Шангри-Ла Молл” тєв, 2-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-453" href="/branches/453">
	<h5 class="card-title">Бага тойруу салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/453.jpg" class="card-img-top" alt="Бага тойруу салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 354660 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	354661 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Их сургуулийн гудамж 3/2, Хуучнаар хvнсний 4-р дэлгvvрийн хойно
</p></div></div></a>

			<a class="branch-card" id="branch-463" href="/branches/463">
	<h5 class="card-title">220 мянгат салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/463.jpg" class="card-img-top" alt="220 мянгат салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7010 0072 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7010 0073 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Чингисийн өргөн чөлөө 13, Натур тур компаний байр 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-470" href="/branches/470">
	<h5 class="card-title">Сэнтрал тауэр салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/470.jpg" class="card-img-top" alt="Сэнтрал тауэр салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7010 0259 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7010 0260 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 8-р хороо, Сvхбаатарын талбайн зvvн урд, Сэнтрал Тауэр, 5-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-473" href="/branches/473">
	<h5 class="card-title">Зуун айл салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/473.jpg" class="card-img-top" alt="Зуун айл салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 352560
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	350391 /Мэдээллийн ажилтан/ &lt;br&gt;
350391 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 10-р хороо, 7-р хороолол, Их тойруу-60, Номт тєвийн байр</p></div></div></a>

			<a class="branch-card" id="branch-495" href="/branches/495">
	<h5 class="card-title">Картын үйлчилгээний төв салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/495.jpg" class="card-img-top" alt="Картын үйлчилгээний төв салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 311112 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Сєvлийн гудамж, М Си Эс Плаза, 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-499" href="/branches/499">
	<h5 class="card-title">Төв салбар </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/499.jpg" class="card-img-top" alt="Төв салбар ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 327020 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	324690 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 14210, 1-р хороо, Энхтайваны єргєн чєлєє 19, ХХБ-ны тєв байр</p></div></div></a>

			<a class="branch-card" id="branch-821" href="/branches/821">
	<h5 class="card-title">11-Р ХОРООЛОЛ TT</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/821.jpg" class="card-img-top" alt="11-Р ХОРООЛОЛ TT">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77078222 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 7-р хороо, 11-р хороолол, Эрхүүгийн гудамж, Этуаль ХХК-ний байр 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-81701" href="/branches/81701">
	<h5 class="card-title">НШШГЕГазрын дэргэдэх тооцооны касс</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/81701.jpg" class="card-img-top" alt="НШШГЕГазрын дэргэдэх тооцооны касс">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 324134 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 5 дугаар хороо, Үндсэн хуулийн гудамж – 3, Нийслэлийн шүүхийн шийдвэр гүйцэтгэх газар</p></div></div></a>

			<a class="branch-card" id="branch-13" href="/branches/13">
	<h5 class="card-title">БАЯНГОЛ ЗОЧИД БУУДАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/13.jpg" class="card-img-top" alt="БАЯНГОЛ ЗОЧИД БУУДАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороо, баянгол зочид буудлын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-24" href="/branches/24">
	<h5 class="card-title">Төв оффис 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/24.jpg" class="card-img-top" alt="Төв оффис 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14210, 1-р хороо, Энхтайваны єргєн чєлєє 19, 1-р эмнэлэгийн хажууд, ХХБ-ны тєв байр
</p></div></div></a>

			<a class="branch-card" id="branch-29" href="/branches/29">
	<h5 class="card-title">ТӨРИЙН ОРДОН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/29.jpg" class="card-img-top" alt="ТӨРИЙН ОРДОН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
6-р хороо, Төрийн ордоны баруун жигүүр, хойд хаалган дээр </p></div></div></a>

			<a class="branch-card" id="branch-47" href="/branches/47">
	<h5 class="card-title">ЦЕНТРАЛ ТАУР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/47.jpg" class="card-img-top" alt="ЦЕНТРАЛ ТАУР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 8-р хороо, Централ тауэр 2 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-52" href="/branches/52">
	<h5 class="card-title">4-Р ДЭЛГҮҮР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/52.jpg" class="card-img-top" alt="4-Р ДЭЛГҮҮР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 6-р хороо, Хуучнаар хүнсний 4-р дэлгүүр дотор, Бага тойруу салбарын урд</p></div></div></a>

			<a class="branch-card" id="branch-53" href="/branches/53">
	<h5 class="card-title">GOTO MARKET </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/53.jpg" class="card-img-top" alt="GOTO MARKET ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 100 айл, Сөүл эмнэлэгийн ард, Go to market худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-57" href="/branches/57">
	<h5 class="card-title">ЗУУН АЙЛ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/57.jpg" class="card-img-top" alt="ЗУУН АЙЛ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
10-р хороо, 7-р хороолол, Их тойруу-60, Номт тєвийн байр, 100 айл салбар дотор</p></div></div></a>

			<a class="branch-card" id="branch-66" href="/branches/66">
	<h5 class="card-title">КАРТЫН ҮЙЛЧИЛГЭЭНИЙ ТӨВ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/66.jpg" class="card-img-top" alt="КАРТЫН ҮЙЛЧИЛГЭЭНИЙ ТӨВ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороо, Сєvлийн гудамж, 1-р сургуулийн замын эсрэг талд, М Си Эс Плаза, 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-68" href="/branches/68">
	<h5 class="card-title">ШҮҮХИЙН ШИЙДВЭР ГҮЙЦЭТГЭХ АЛБА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/68.jpg" class="card-img-top" alt="ШҮҮХИЙН ШИЙДВЭР ГҮЙЦЭТГЭХ АЛБА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:30-20:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 5-р хороо, Нарны гүүрний хажууд, Нийслэлийн Шийдвэр Гүйцэтгэх Албаны 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-75" href="/branches/75">
	<h5 class="card-title">АТЛАС 100 АЙЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/75.jpg" class="card-img-top" alt="АТЛАС 100 АЙЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 11-р хороо, 100 айл, Атлас центр 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-83" href="/branches/83">
	<h5 class="card-title">ДАМБАДАРЖАА ХАН-ЭРДЭНЭ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/83.jpg" class="card-img-top" alt="ДАМБАДАРЖАА ХАН-ЭРДЭНЭ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 15-р хороо, Дамба явах замд, Миний дэлгүүрийн зүүн талд, Хан-эрдэнэ дэлгүүр дотор</p></div></div></a>

			<a class="branch-card" id="branch-110" href="/branches/110">
	<h5 class="card-title">БАГА ТОЙРУУ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/110.jpg" class="card-img-top" alt="БАГА ТОЙРУУ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Их сургуулийн гудамж 3/2, Хуучнаар хvнсний 4-р дэлгvvрийн хойно</p></div></div></a>

			<a class="branch-card" id="branch-120" href="/branches/120">
	<h5 class="card-title">АВТО ПЛАЗА 1</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/120.jpg" class="card-img-top" alt="АВТО ПЛАЗА 1">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
100 айл АВТОПЛАЗА-1 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-121" href="/branches/121">
	<h5 class="card-title">НАРАН ПЛАЗА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/121.jpg" class="card-img-top" alt="НАРАН ПЛАЗА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Энхтайваны гүүрний хойно, НАРАН ПЛАЗА, 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-124" href="/branches/124">
	<h5 class="card-title">ЛЕНИН КЛУБ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/124.jpg" class="card-img-top" alt="ЛЕНИН КЛУБ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сүхбаатарын талбайн урд талын автобусны буудлын ард</p></div></div></a>

			<a class="branch-card" id="branch-125" href="/branches/125">
	<h5 class="card-title">ЛЕНИН КЛУБ 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/125.jpg" class="card-img-top" alt="ЛЕНИН КЛУБ 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сүхбаатарын талбайн урд талын автобусны буудлын ард</p></div></div></a>

			<a class="branch-card" id="branch-136" href="/branches/136">
	<h5 class="card-title">МЕТРОМОЛЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/136.jpg" class="card-img-top" alt="МЕТРОМОЛЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, СУИС-н замын эсрэг талд, МETROMALL дэлгүүрийн В1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-145" href="/branches/145">
	<h5 class="card-title">АВТОМОЛЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/145.jpg" class="card-img-top" alt="АВТОМОЛЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Автомоллын В1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-154" href="/branches/154">
	<h5 class="card-title">СӨҮЛ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/154.jpg" class="card-img-top" alt="СӨҮЛ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сєvлийн гудамж, 33-р байр, Хэрлэн Плаза 2-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-158" href="/branches/158">
	<h5 class="card-title">ЗЭЛМЭ ТӨВ ДАМБА ЭЦЭС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/158.jpg" class="card-img-top" alt="ЗЭЛМЭ ТӨВ ДАМБА ЭЦЭС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 15-Р ХОРОО, ДАМБАДАРЖАА ХУУЧИН ЭЦЭС ЗЭЛМЭ ТӨВ
</p></div></div></a>

			<a class="branch-card" id="branch-159" href="/branches/159">
	<h5 class="card-title">ЮНИОН БЮЛДИНГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/159.jpg" class="card-img-top" alt="ЮНИОН БЮЛДИНГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Буянгын зам Юнион бюлдинг 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-165" href="/branches/165">
	<h5 class="card-title">СБД ЗДТГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/165.jpg" class="card-img-top" alt="СБД ЗДТГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 7-Р ХОРОО, СБД-ийн байран дотор</p></div></div></a>

			<a class="branch-card" id="branch-179" href="/branches/179">
	<h5 class="card-title">САРУУЛ МАРКЕТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/179.jpg" class="card-img-top" alt="САРУУЛ МАРКЕТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сүхбаатар дүүрэг, 3-р хороо, Саруул маркет, төв хаалганы хажууд</p></div></div></a>

			<a class="branch-card" id="branch-180" href="/branches/180">
	<h5 class="card-title">ТӨВ САЛБАР-1</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/180.jpg" class="card-img-top" alt="ТӨВ САЛБАР-1">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14210, 1-р хороо, Энхтайваны єргєн чєлєє 19,1-р эмнэлэгийн хажууд, ХХБ-ны тєв байр</p></div></div></a>

			<a class="branch-card" id="branch-219" href="/branches/219">
	<h5 class="card-title">220 МЯНГАТ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/219.jpg" class="card-img-top" alt="220 МЯНГАТ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороо, Чингисийн өргөн чөлөө 13, Натур тур компаний байр 1 давхар /220 мянгат салбар дотор/
</p></div></div></a>

			<a class="branch-card" id="branch-221" href="/branches/221">
	<h5 class="card-title">НОМИН АЗ ЖАРГАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/221.jpg" class="card-img-top" alt="НОМИН АЗ ЖАРГАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сүхбаатар дүүрэг, 11-р хороо Аз жаргал хотхон, Номин супермаркет, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-227" href="/branches/227">
	<h5 class="card-title">АТМ СӨҮЛИЙН ГУДАМЖ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/227.jpg" class="card-img-top" alt="АТМ СӨҮЛИЙН ГУДАМЖ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 3-р хороо, Хэрлэн плазагийн эсрэг талд, зам дагуу
</p></div></div></a>

			<a class="branch-card" id="branch-95800033" href="/branches/95800033">
	<h5 class="card-title">KYOTO MEDICAL SALON (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800033.jpg" class="card-img-top" alt="KYOTO MEDICAL SALON (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			76100130
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Twin tower</p></div></div></a>

			<a class="branch-card" id="branch-95800036" href="/branches/95800036">
	<h5 class="card-title">БАТБАЙГАЛЬ БЭЙКЭРИ ( Discount 2% , 2% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800036.jpg" class="card-img-top" alt="БАТБАЙГАЛЬ БЭЙКЭРИ ( Discount 2% , 2% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11462629
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Герман элчингийн хажууд</p></div></div></a>

			<a class="branch-card" id="branch-95800038" href="/branches/95800038">
	<h5 class="card-title">CHARMING BEAUTY SALON ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800038.jpg" class="card-img-top" alt="CHARMING BEAUTY SALON ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77339999
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Grand Khan Irish</p></div></div></a>

			<a class="branch-card" id="branch-95800039" href="/branches/95800039">
	<h5 class="card-title">DELHI DARBAR ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800039.jpg" class="card-img-top" alt="DELHI DARBAR ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11326543
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
CБД 4-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800040" href="/branches/95800040">
	<h5 class="card-title">DELHI DARBAR ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800040.jpg" class="card-img-top" alt="DELHI DARBAR ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11326543
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Puma Imperial</p></div></div></a>

			<a class="branch-card" id="branch-95800041" href="/branches/95800041">
	<h5 class="card-title">ECLIPSE RESTAURANT ( Discount 5% , 8% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800041.jpg" class="card-img-top" alt="ECLIPSE RESTAURANT ( Discount 5% , 8% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77006060
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Тусгаар тогтнолын ордон</p></div></div></a>

			<a class="branch-card" id="branch-95800043" href="/branches/95800043">
	<h5 class="card-title">ЭВСЭГ ХК ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800043.jpg" class="card-img-top" alt="ЭВСЭГ ХК ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11343595
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
CБД 4-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800044" href="/branches/95800044">
	<h5 class="card-title">ЭВСЭГ ХК ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800044.jpg" class="card-img-top" alt="ЭВСЭГ ХК ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11343595
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, UB mart, 2-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-95800046" href="/branches/95800046">
	<h5 class="card-title">ЭВСЭГ ХК ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800046.jpg" class="card-img-top" alt="ЭВСЭГ ХК ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11343595
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Наран Молл</p></div></div></a>

			<a class="branch-card" id="branch-95800051" href="/branches/95800051">
	<h5 class="card-title">GOBI ( Discount 3% , 4% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800051.jpg" class="card-img-top" alt="GOBI ( Discount 3% , 4% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11320303
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Талбайн урд</p></div></div></a>

			<a class="branch-card" id="branch-95800053" href="/branches/95800053">
	<h5 class="card-title">GOBI ( Discount 3% , 4% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800053.jpg" class="card-img-top" alt="GOBI ( Discount 3% , 4% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11320303
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Шангри-ла молл, YAMA Кашимер</p></div></div></a>

			<a class="branch-card" id="branch-95800056" href="/branches/95800056">
	<h5 class="card-title">ХОНХОНДОЙ ЭМИЙН САН ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800056.jpg" class="card-img-top" alt="ХОНХОНДОЙ ЭМИЙН САН ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11327573
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 1-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800059" href="/branches/95800059">
	<h5 class="card-title">LHAMOUR ( Discount 3% , 8% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800059.jpg" class="card-img-top" alt="LHAMOUR ( Discount 3% , 8% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77120256
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Шангри-ла молл</p></div></div></a>

			<a class="branch-card" id="branch-95800062" href="/branches/95800062">
	<h5 class="card-title">MY BOUTIQUE ( Discount 5% , 10% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800062.jpg" class="card-img-top" alt="MY BOUTIQUE ( Discount 5% , 10% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11325994
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Metromall</p></div></div></a>

			<a class="branch-card" id="branch-95800063" href="/branches/95800063">
	<h5 class="card-title">MY BOUTIQUE ( Discount 5% , 10% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800063.jpg" class="card-img-top" alt="MY BOUTIQUE ( Discount 5% , 10% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11325994
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 1-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800068" href="/branches/95800068">
	<h5 class="card-title">MINI BRAVO ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800068.jpg" class="card-img-top" alt="MINI BRAVO ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70136483
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 1-р төрх</p></div></div></a>

			<a class="branch-card" id="branch-95800077" href="/branches/95800077">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800077.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Metromall</p></div></div></a>

			<a class="branch-card" id="branch-95800086" href="/branches/95800086">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800086.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Авто плазагийн зүүн талд</p></div></div></a>

			<a class="branch-card" id="branch-95800094" href="/branches/95800094">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800094.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 2-р хороо Далай ээж</p></div></div></a>

			<a class="branch-card" id="branch-95800104" href="/branches/95800104">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800104.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 6 буудал Оргил төв</p></div></div></a>

			<a class="branch-card" id="branch-95800107" href="/branches/95800107">
	<h5 class="card-title">YVES ROCHE ( Discount 2% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800107.jpg" class="card-img-top" alt="YVES ROCHE ( Discount 2% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11327683
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Наран плаза</p></div></div></a>

			<a class="branch-card" id="branch-95800108" href="/branches/95800108">
	<h5 class="card-title">YVES ROCHE ( Discount 2% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800108.jpg" class="card-img-top" alt="YVES ROCHE ( Discount 2% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11327683
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Шангри-ла молл</p></div></div></a>

			<a class="branch-card" id="branch-95800109" href="/branches/95800109">
	<h5 class="card-title">YVES ROCHE ( Discount 2% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800109.jpg" class="card-img-top" alt="YVES ROCHE ( Discount 2% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11327683
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Наран Молл</p></div></div></a>

			<a class="branch-card" id="branch-95800110" href="/branches/95800110">
	<h5 class="card-title">THANN SHOP ( Discount 2% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800110.jpg" class="card-img-top" alt="THANN SHOP ( Discount 2% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70107683
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Наран плаза</p></div></div></a>

			<a class="branch-card" id="branch-95800111" href="/branches/95800111">
	<h5 class="card-title">THANN SHOP ( Discount 2% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800111.jpg" class="card-img-top" alt="THANN SHOP ( Discount 2% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70107683
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Наран Молл</p></div></div></a>

			<a class="branch-card" id="branch-95800113" href="/branches/95800113">
	<h5 class="card-title">PEA BERRY COFFEE SHOP ( Discount 10% , 10% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800113.jpg" class="card-img-top" alt="PEA BERRY COFFEE SHOP ( Discount 10% , 10% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			88084167
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Сөүлийн гудамж</p></div></div></a>

			<a class="branch-card" id="branch-95800114" href="/branches/95800114">
	<h5 class="card-title">PETIT BATEAU ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800114.jpg" class="card-img-top" alt="PETIT BATEAU ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77112888
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Central tower</p></div></div></a>

			<a class="branch-card" id="branch-95800116" href="/branches/95800116">
	<h5 class="card-title">САРНАЙХ BEAUTY SALON ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800116.jpg" class="card-img-top" alt="САРНАЙХ BEAUTY SALON ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70111727
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 1-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800121" href="/branches/95800121">
	<h5 class="card-title">SEA BERRY ( Discount 4% , 7% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800121.jpg" class="card-img-top" alt="SEA BERRY ( Discount 4% , 7% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70070078
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 1-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800122" href="/branches/95800122">
	<h5 class="card-title">SEOUL OPTICS ( Discount 10% , 10% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800122.jpg" class="card-img-top" alt="SEOUL OPTICS ( Discount 10% , 10% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			91111288
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД UB mart</p></div></div></a>

			<a class="branch-card" id="branch-95800127" href="/branches/95800127">
	<h5 class="card-title">SPRINGS HOTEL ( Discount 4% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800127.jpg" class="card-img-top" alt="SPRINGS HOTEL ( Discount 4% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70119191
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Эрүүл мэндийн яам</p></div></div></a>

			<a class="branch-card" id="branch-95800128" href="/branches/95800128">
	<h5 class="card-title">SQUARE GRILL PUB ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800128.jpg" class="card-img-top" alt="SQUARE GRILL PUB ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11313355
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сүхбаатар дүүрэг, 8-р хороо, Централ тауэр, 3-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-95800131" href="/branches/95800131">
	<h5 class="card-title">TESCOMA SHOP ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800131.jpg" class="card-img-top" alt="TESCOMA SHOP ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11328286
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Grand office</p></div></div></a>

			<a class="branch-card" id="branch-95800134" href="/branches/95800134">
	<h5 class="card-title">TOY LAND SHOP ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800134.jpg" class="card-img-top" alt="TOY LAND SHOP ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			91990972
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 4-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800135" href="/branches/95800135">
	<h5 class="card-title">WOLFORD SHOP ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800135.jpg" class="card-img-top" alt="WOLFORD SHOP ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77016888
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Central tower</p></div></div></a>

			<a class="branch-card" id="branch-95800137" href="/branches/95800137">
	<h5 class="card-title">UNITED COLORS OF BENETTON (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800137.jpg" class="card-img-top" alt="UNITED COLORS OF BENETTON (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77035050
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Улаанбаатар Их Дэлгүүр</p></div></div></a>

			<a class="branch-card" id="branch-95800140" href="/branches/95800140">
	<h5 class="card-title">FEATHER LEAF SALON (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800140.jpg" class="card-img-top" alt="FEATHER LEAF SALON (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77017799
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД 8-р хороо Сentral Tower</p></div></div></a>

			<a class="branch-card" id="branch-95800141" href="/branches/95800141">
	<h5 class="card-title">DYRBERG KERN (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800141.jpg" class="card-img-top" alt="DYRBERG KERN (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			93113993
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Шангри-ла молл</p></div></div></a>

			<a class="branch-card" id="branch-42" href="/branches/42">
	<h5 class="card-title">УБ ИХ ДЭЛГҮҮР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/42.jpg" class="card-img-top" alt="УБ ИХ ДЭЛГҮҮР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 3-р хороо, Улаанбаатар их дэлгүүрийн В1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-45" href="/branches/45">
	<h5 class="card-title">САНСАР 32</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/45.jpg" class="card-img-top" alt="САНСАР 32">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
12-р хороо, 32-ын тойрог сансар худалдааны төвийн 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-46" href="/branches/46">
	<h5 class="card-title">МОННИС ТАУР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/46.jpg" class="card-img-top" alt="МОННИС ТАУР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Улаанбаатар хот, Сүхбаатар дүүрэг Моннис цамхагын 1 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-70" href="/branches/70">
	<h5 class="card-title">ШАНГРИ-ЛА САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/70.jpg" class="card-img-top" alt="ШАНГРИ-ЛА САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороо, Олимпийн гудамж - 19, “Шангри-Ла Молл” тєв, 2-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-77" href="/branches/77">
	<h5 class="card-title">ШАНГРИ ЛА МОЛЛ B1 ДАВХАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/77.jpg" class="card-img-top" alt="ШАНГРИ ЛА МОЛЛ B1 ДАВХАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Олимпийн гудамж - 19, “Шангри-Ла Молл” тєв, B1 давхар
</p></div></div></a>

			<a class="branch-card" id="branch-79" href="/branches/79">
	<h5 class="card-title">ДӨЧИН МЯНГАТ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/79.jpg" class="card-img-top" alt="ДӨЧИН МЯНГАТ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-19:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
4-р хороо, Сєvлийн гудамж, хуучнаар Хүнсний 50-р дэлгүүр, 1 давхар, 40 мянгат салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-106" href="/branches/106">
	<h5 class="card-title">ТӨВ САЛБАР-2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/106.jpg" class="card-img-top" alt="ТӨВ САЛБАР-2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14210, 1-р хороо, Энхтайваны єргєн чєлєє 19, 1-р эмнэлэгийн хажууд, ХХБ-ны тєв байр
</p></div></div></a>

			<a class="branch-card" id="branch-112" href="/branches/112">
	<h5 class="card-title">ТӨВ САЛБАР - 3</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/112.jpg" class="card-img-top" alt="ТӨВ САЛБАР - 3">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14210, 1-р хороо, Энхтайваны єргєн чєлєє 19, 1-р эмнэлэгийн хажууд, ХХБ-ны тєв байр
</p></div></div></a>

			<a class="branch-card" id="branch-167" href="/branches/167">
	<h5 class="card-title">НОМИН ЭТУАЛЬ ТӨВ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/167.jpg" class="card-img-top" alt="НОМИН ЭТУАЛЬ ТӨВ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 7-Р ХОРОО, ЭРХҮҮГИЙН ГУДАМЖ, ЭТУАЛЬ ТӨВ, 11-р хороолол тооцооны төвийн үүдэнд  
</p></div></div></a>

			<a class="branch-card" id="branch-175" href="/branches/175">
	<h5 class="card-title">БАГА ТОЙРУУ САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/175.jpg" class="card-img-top" alt="БАГА ТОЙРУУ САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Их сургуулийн гудамж 3/2, Хуучнаар хvнсний 4-р дэлгvvрийн хойно, Бага тойруу салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-185" href="/branches/185">
	<h5 class="card-title">ИХ НАЯД ПЛАЗА 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/185.jpg" class="card-img-top" alt="ИХ НАЯД ПЛАЗА 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Их наяд худалдааны төв 1 давхар /салбарын үүдэнд/
</p></div></div></a>

			<a class="branch-card" id="branch-216" href="/branches/216">
	<h5 class="card-title">БАЯЛАГ УНДРАА ЗАХ 3</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/216.jpg" class="card-img-top" alt="БАЯЛАГ УНДРАА ЗАХ 3">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Ням:</strong>
					11:00-19:30
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БЗД, 14-р хороо, Нарантуул зах, Баялаг ундраа захын 1 давхарт баруун хаалган дээр 
</p></div></div></a>

			<a class="branch-card" id="branch-411" href="/branches/411">
	<h5 class="card-title">Чингэлтэй салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/411.jpg" class="card-img-top" alt="Чингэлтэй салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			313833 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	311994 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Бага тойруу - 17, "Зоос гоёл" ХХК-ийн байр, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-413" href="/branches/413">
	<h5 class="card-title">Жуулчин салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/413.jpg" class="card-img-top" alt="Жуулчин салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям:</strong>
					10:00-16:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75050690 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75050680 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 15170, 40 мянгат 8б байр</p></div></div></a>

			<a class="branch-card" id="branch-419" href="/branches/419">
	<h5 class="card-title">Пийс тауэр салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/419.jpg" class="card-img-top" alt="Пийс тауэр салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7000 6927
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70006928 /Мэдээллийн ажилтан/ &lt;br&gt;
70006929 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 3-р хороо, Энхтайваны өргөн чөлөө-54, Пийс молл, 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-431" href="/branches/431">
	<h5 class="card-title">М Плаза салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/431.jpg" class="card-img-top" alt="М Плаза салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7011-0333 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7011-0335 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 5-р хороо, Самбуугийн гудамж-24, “М Плаза” тєв, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-433" href="/branches/433">
	<h5 class="card-title">Бөмбөгөр салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/433.jpg" class="card-img-top" alt="Бөмбөгөр салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70003433 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70005433 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 2-р хороо, Бөмбөгөр худалдааны төвийн зүүн талд 27/4 байр, 2-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-452" href="/branches/452">
	<h5 class="card-title">Занабазар салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/452.jpg" class="card-img-top" alt="Занабазар салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 312356 /Мэдээллийн ажилтан/ &lt;br&gt;
328531
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	329413 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Худалдааны гудамж-7, Барилгачдын талбайн урд</p></div></div></a>

			<a class="branch-card" id="branch-472" href="/branches/472">
	<h5 class="card-title">Гандирс салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/472.jpg" class="card-img-top" alt="Гандирс салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 316545 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	&nbsp;316544 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Улсын их дэлгvvрийн зvvн талд, "Гандирс" тєв, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-800" href="/branches/800">
	<h5 class="card-title">ТАЛБАЙ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/800.jpg" class="card-img-top" alt="ТАЛБАЙ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			319041 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	321149 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 15160, Самбуугийн гудамж, Бага тойруу 15, Хөдөлмөрийн ордон, 1-р давхарт </p></div></div></a>

			<a class="branch-card" id="branch-811" href="/branches/811">
	<h5 class="card-title">УЛААНБААТАР САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/811.jpg" class="card-img-top" alt="УЛААНБААТАР САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			312155 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	320527 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 15160, Самбуугийн гудамж, Бага тойруу 15, Хөдөлмөрийн ордон, 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-3" href="/branches/3">
	<h5 class="card-title">7 БУУДАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3.jpg" class="card-img-top" alt="7 БУУДАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Долоон Буудлын Зам, автобусны буудлын баруун талд, Сайн ломбардны үүдэнд 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-8" href="/branches/8">
	<h5 class="card-title">М ПЛАЗА ТЭНГИС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/8.jpg" class="card-img-top" alt="М ПЛАЗА ТЭНГИС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 5-р хороо, Самбуугийн гудамж-24, М Плаза тєв, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-27" href="/branches/27">
	<h5 class="card-title">НАРЛАГ ДЭНЖ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/27.jpg" class="card-img-top" alt="НАРЛАГ ДЭНЖ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
11-р хороо,  нарлаг дэнж худалдааны төвийн хашаан дотор </p></div></div></a>

			<a class="branch-card" id="branch-90" href="/branches/90">
	<h5 class="card-title">АЛТАЙ ЦЕНТР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/90.jpg" class="card-img-top" alt="АЛТАЙ ЦЕНТР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-20:00
				<br>
								<strong>Бям-Ням:</strong>
					11:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД,  УИД-н хажууд Алтай Центрийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-91" href="/branches/91">
	<h5 class="card-title">УБХБ ШИЛЭН БАНК</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/91.jpg" class="card-img-top" alt="УБХБ ШИЛЭН БАНК">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 15160, Самбуугийн гудамж, Бага тойруу 15, Зоос гоёлын эсрэг талд, Улаанбаатар салбарын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-101" href="/branches/101">
	<h5 class="card-title">УБ БАНК 2-Р ТТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/101.jpg" class="card-img-top" alt="УБ БАНК 2-Р ТТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:30-20:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, Жуулчин салбарын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-103" href="/branches/103">
	<h5 class="card-title">АЛТЖИН БӨМБӨГӨР 1</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/103.jpg" class="card-img-top" alt="АЛТЖИН БӨМБӨГӨР 1">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Ням:</strong>
					11:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Алтжин худалдааны төвийн 1 давхарт, баруун урд хаалга 
</p></div></div></a>

			<a class="branch-card" id="branch-123" href="/branches/123">
	<h5 class="card-title">АЛТЖИН БӨМБӨГӨР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/123.jpg" class="card-img-top" alt="АЛТЖИН БӨМБӨГӨР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					11:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Алтжин худалдааны төвийн 1 давхарт, баруун хойд талд
</p></div></div></a>

			<a class="branch-card" id="branch-152" href="/branches/152">
	<h5 class="card-title">ПИЙС ТАУЭР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/152.jpg" class="card-img-top" alt="ПИЙС ТАУЭР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 3 Хороо, Пийс тауэрын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-157" href="/branches/157">
	<h5 class="card-title">ЗАНАБАЗАР 1</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/157.jpg" class="card-img-top" alt="ЗАНАБАЗАР 1">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 1-р хороо, Занабазар салбарын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-170" href="/branches/170">
	<h5 class="card-title">ТӨВ ТАЛБАЙ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/170.jpg" class="card-img-top" alt="ТӨВ ТАЛБАЙ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р, хороо, 15160, Д.Сүхбаатарын талбай 11, Хөдөлмөрчдийн ордоны 1 давхарт,  Төв талбай салбарын үүдэнд</p></div></div></a>

			<a class="branch-card" id="branch-204" href="/branches/204">
	<h5 class="card-title">Компьютер моол</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/204.jpg" class="card-img-top" alt="Компьютер моол">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 9-р хороо Компьютер моол худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-205" href="/branches/205">
	<h5 class="card-title">ХӨТӨЛ СУПЕРМАРКЕТ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/205.jpg" class="card-img-top" alt="ХӨТӨЛ СУПЕРМАРКЕТ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД Баянхошууны хөтлийн буудал Хөтөл супермаркет</p></div></div></a>

			<a class="branch-card" id="branch-209" href="/branches/209">
	<h5 class="card-title">CU 1-Р ДЭЛГҮҮР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/209.jpg" class="card-img-top" alt="CU 1-Р ДЭЛГҮҮР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД Хуучнаар хүнсний 1-р дэлгүүрийн байранд, CU дотор</p></div></div></a>

			<a class="branch-card" id="branch-223" href="/branches/223">
	<h5 class="card-title">БҮРЭН ПЛАЗА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/223.jpg" class="card-img-top" alt="БҮРЭН ПЛАЗА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Чингэлтэй дүүрэг, 7-н буудлын эцэс, Бүрэн плаза, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-235" href="/branches/235">
	<h5 class="card-title">АТМ ЮМТ БӨМБӨГӨР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/235.jpg" class="card-img-top" alt="АТМ ЮМТ БӨМБӨГӨР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 2-р хороо Бөмбөгөр-1 худалдааны төв, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-236" href="/branches/236">
	<h5 class="card-title">АТМ НАРАНТУУЛ-2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/236.jpg" class="card-img-top" alt="АТМ НАРАНТУУЛ-2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 12-р хороо, Нарантуул-2 худалдааны төв, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-241" href="/branches/241">
	<h5 class="card-title">НҮҮР АМ СУДЛАЛЫН СУРГУУЛЬ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/241.jpg" class="card-img-top" alt="НҮҮР АМ СУДЛАЛЫН СУРГУУЛЬ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 11-р хороо, 32-н тойрог дээр, Нүүр ам судлалын сургуулийн эмнэлэгийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-95800047" href="/branches/95800047">
	<h5 class="card-title">ЭВСЭГ ХК ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800047.jpg" class="card-img-top" alt="ЭВСЭГ ХК ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11343595
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД Cashmere house</p></div></div></a>

			<a class="branch-card" id="branch-95800055" href="/branches/95800055">
	<h5 class="card-title">ХОНХОНДОЙ ЭМИЙН САН ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800055.jpg" class="card-img-top" alt="ХОНХОНДОЙ ЭМИЙН САН ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11327573
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД 1-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800058" href="/branches/95800058">
	<h5 class="card-title">KHURLEE HAIR SALON ( Discount 2% , 2% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800058.jpg" class="card-img-top" alt="KHURLEE HAIR SALON ( Discount 2% , 2% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11323048
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Чингэлтэй дүүрэг, 3-р хороо, Алтай төв, 5-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-95800064" href="/branches/95800064">
	<h5 class="card-title">MY BOUTIQUE ( Discount 5% , 10% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800064.jpg" class="card-img-top" alt="MY BOUTIQUE ( Discount 5% , 10% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11325994
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Peace tower</p></div></div></a>

			<a class="branch-card" id="branch-95800065" href="/branches/95800065">
	<h5 class="card-title">MARC SHOP ( Discount 3% , 6% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800065.jpg" class="card-img-top" alt="MARC SHOP ( Discount 3% , 6% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			98115909
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Барилгачдын талбай</p></div></div></a>

			<a class="branch-card" id="branch-95800078" href="/branches/95800078">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800078.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД 2-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800089" href="/branches/95800089">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800089.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД Тавин мянгат</p></div></div></a>

			<a class="branch-card" id="branch-21" href="/branches/21">
	<h5 class="card-title">ПАРК ОД МОЛЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/21.jpg" class="card-img-top" alt="ПАРК ОД МОЛЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					09:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
26-р хороо, Парк-од молл худалдаа, үйлчилгээний төв 1 давхарт 

</p></div></div></a>

			<a class="branch-card" id="branch-41" href="/branches/41">
	<h5 class="card-title">ТЭДИ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/41.jpg" class="card-img-top" alt="ТЭДИ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, Теди төв 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-78" href="/branches/78">
	<h5 class="card-title">ЧИНГЭЛТЭЙ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/78.jpg" class="card-img-top" alt="ЧИНГЭЛТЭЙ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Бага тойруу - 17, "Зоос гоёл" ХХК-ийн байр, 1-р давхар, Чингэлтэй салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-87" href="/branches/87">
	<h5 class="card-title">ГАНДИРС САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/87.jpg" class="card-img-top" alt="ГАНДИРС САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Улсын их дэлгvvрийн зvvн талд, "Гандирс" тєв, 1-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-143" href="/branches/143">
	<h5 class="card-title">Бөмбөгөр салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/143.jpg" class="card-img-top" alt="Бөмбөгөр салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
2-р хороо, Бөмбөгөр худалдааны төвийн зүүн талд 27/4 байр , 2давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-181" href="/branches/181">
	<h5 class="card-title">М ПЛАЗА САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/181.jpg" class="card-img-top" alt="М ПЛАЗА САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
5-р хороо, Самбуугийн гудамж-24, “М Плаза” тєв, 1-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-195" href="/branches/195">
	<h5 class="card-title">СОДОН БӨМБӨГӨР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/195.jpg" class="card-img-top" alt="СОДОН БӨМБӨГӨР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Чингэлтэй дүүрэг, 2-хороо, Содон бөмбөгөр худалдааны төвийн урд хаалган дээр 
</p></div></div></a>

			<a class="branch-card" id="branch-197" href="/branches/197">
	<h5 class="card-title">ЗАНАБАЗАР САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/197.jpg" class="card-img-top" alt="ЗАНАБАЗАР САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Худалдааны гудамж-7, Барилгачдын талбайн урд, Занабазар салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-405" href="/branches/405">
	<h5 class="card-title">Төмөр зам салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/405.jpg" class="card-img-top" alt="Төмөр зам салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			254867 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	254869 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 1-р хороо, Тээвэрчдийн гудамж, "УБТЗ"-ын Улаанбаатар худалдааны тєв</p></div></div></a>

			<a class="branch-card" id="branch-439" href="/branches/439">
	<h5 class="card-title">Макс моол салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/439.jpg" class="card-img-top" alt="Макс моол салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70000093 /Мэдээллийн ажилтан /
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70000092 /Зээлийн мэргэжилтэн /<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянгол дүүрэг 16-р хороо, Энхтайваны өргөн чөлөө-35, Макс моол худалдааны төв 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-456" href="/branches/456">
	<h5 class="card-title">Өргөө салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/456.jpg" class="card-img-top" alt="Өргөө салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям:</strong>
					11:00-17:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 361968 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	368961 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 13-р хороо, Ард Аюушийн єргєн чєлєє гудамж, Өргөө салбар</p></div></div></a>

			<a class="branch-card" id="branch-460" href="/branches/460">
	<h5 class="card-title">Гранд салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/460.jpg" class="card-img-top" alt="Гранд салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7014 0460 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70140461 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, Баруун 4-н зам, Гранд плаза, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-461" href="/branches/461">
	<h5 class="card-title">Баянгол-Имарт салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/461.jpg" class="card-img-top" alt="Баянгол-Имарт салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75700461 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75700561 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 6-р хороо, Имарт-Баянгол худалдааны төвийн 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-475" href="/branches/475">
	<h5 class="card-title">Эрдэнэс салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/475.jpg" class="card-img-top" alt="Эрдэнэс салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям:</strong>
					Амарна
				<br>
								<strong>Ням:</strong>
					11:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7011 4982 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7011 4987 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 3-р хороолол, 15-р хороо, Л.Энэбишийн єргєн чєлєє</p></div></div></a>

			<a class="branch-card" id="branch-801" href="/branches/801">
	<h5 class="card-title">Техник импорт тооцооны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/801.jpg" class="card-img-top" alt="Техник импорт тооцооны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7017 8222 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 5-р хороо, Энхтайваны өргөн чөлөө 125, Техник Импорт ХК 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-802" href="/branches/802">
	<h5 class="card-title">ТҮМЭН ПЛАЗА САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/802.jpg" class="card-img-top" alt="ТҮМЭН ПЛАЗА САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			302622 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 14- хороо, Ард-Аюушийн өргөн чөлөө-5</p></div></div></a>

			<a class="branch-card" id="branch-824" href="/branches/824">
	<h5 class="card-title">4-р хороолол TT</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/824.jpg" class="card-img-top" alt="4-р хороолол TT">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75058223 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 11-р хороо, 4-р хороолол, Энэбишийн гудамж, ОЧИР хотхон 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-80103" href="/branches/80103">
	<h5 class="card-title">ГУРВАЛЖИН ТООЦООНЫ КАСС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/80103.jpg" class="card-img-top" alt="ГУРВАЛЖИН ТООЦООНЫ КАСС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70178222 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 5-р хороо, Ти Ай Ложистик ххк, 1-р давхарт </p></div></div></a>

			<a class="branch-card" id="branch-4" href="/branches/4">
	<h5 class="card-title">ВОКЗАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/4.jpg" class="card-img-top" alt="ВОКЗАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					07:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД - 1 хороо, Улаанбаатар төмөр зам, 1 давхарт, кассын хажууд</p></div></div></a>

			<a class="branch-card" id="branch-9" href="/branches/9">
	<h5 class="card-title">ХАРХОРИН ЗАХЫН САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/9.jpg" class="card-img-top" alt="ХАРХОРИН ЗАХЫН САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					09:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороолол, 20-р хороо, Москвагийн гудамж, Хархорин Худалдааны тєв, 1-р давхар, салбарын үүдэнд</p></div></div></a>

			<a class="branch-card" id="branch-23" href="/branches/23">
	<h5 class="card-title">ГРАНД ПЛАЗА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/23.jpg" class="card-img-top" alt="ГРАНД ПЛАЗА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баруун 4-н зам, Гранд плаза, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-26" href="/branches/26">
	<h5 class="card-title">ТӨМӨР ЗАМ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/26.jpg" class="card-img-top" alt="ТӨМӨР ЗАМ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороо, Тээвэрчдийн гудамж, "УБТЗ"-ын Улаанбаатар худалдааны тєв</p></div></div></a>

			<a class="branch-card" id="branch-30" href="/branches/30">
	<h5 class="card-title">НОМИН ПЛАЗА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/30.jpg" class="card-img-top" alt="НОМИН ПЛАЗА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-19:00
				<br>
								<strong>Бям-Ням:</strong>
					10:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14-р хороо Өргөөгийн хажууд, Номин их дэлгүүр, В1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-31" href="/branches/31">
	<h5 class="card-title">ХАНБҮРГЭДЭЙ ИХ ДЭЛГҮҮР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/31.jpg" class="card-img-top" alt="ХАНБҮРГЭДЭЙ ИХ ДЭЛГҮҮР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 4-р хороо, Ханбүргэдэй дэлгүүр, 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-33" href="/branches/33">
	<h5 class="card-title">ДЦС-4</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/33.jpg" class="card-img-top" alt="ДЦС-4">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 5-р хороо, ТЭЦ 4, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-40" href="/branches/40">
	<h5 class="card-title">ӨРГӨӨ 1 КИНОТЕАТР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/40.jpg" class="card-img-top" alt="ӨРГӨӨ 1 КИНОТЕАТР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, Өргөө кино театр, 1 давхарт, зүүн талд</p></div></div></a>

			<a class="branch-card" id="branch-51" href="/branches/51">
	<h5 class="card-title">НОМИН ӨНӨР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/51.jpg" class="card-img-top" alt="НОМИН ӨНӨР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-19:00
				<br>
								<strong>Бям:</strong>
					Амарна
				<br>
								<strong>Ням:</strong>
					11:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
20-р хороо, Төв замын урд, Номин өнөр үйлчилгээний төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-54" href="/branches/54">
	<h5 class="card-title">ГАНДАН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/54.jpg" class="card-img-top" alt="ГАНДАН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЧД, 16-р хороо, Гандантэгчилэн хийд, кассын хажууд 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-59" href="/branches/59">
	<h5 class="card-title">ТЕХНИК ИМПОРТ ТТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/59.jpg" class="card-img-top" alt="ТЕХНИК ИМПОРТ ТТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 5-р хороо, Энхтайваны өргөн чөлөө 125, Саппорогийн уулзвар дээр, Техник Импорт ХК 1-р давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-62" href="/branches/62">
	<h5 class="card-title">БАРС 2 ЗАХ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/62.jpg" class="card-img-top" alt="БАРС 2 ЗАХ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 3-р хороо,Хархорин захын хажууд,  Барс -2 зах худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-67" href="/branches/67">
	<h5 class="card-title">ТБД АНДУУД СТАРС ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/67.jpg" class="card-img-top" alt="ТБД АНДУУД СТАРС ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 2-р хороо, ТБД андуудын 1 давхарт,  зүүн талд</p></div></div></a>

			<a class="branch-card" id="branch-71" href="/branches/71">
	<h5 class="card-title">ОРГИЛ СУПЕРМАРКЕТ ХОРООЛОЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/71.jpg" class="card-img-top" alt="ОРГИЛ СУПЕРМАРКЕТ ХОРООЛОЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 13-р хороо, 3-р хорооллын эцэст, Соло моллын баруун талд Оргил супермаркет 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-72" href="/branches/72">
	<h5 class="card-title">МОСКВА ИХ ДЭЛГҮҮР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/72.jpg" class="card-img-top" alt="МОСКВА ИХ ДЭЛГҮҮР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					11:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 14-р хороо, Москва их дэлгүүрийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-81" href="/branches/81">
	<h5 class="card-title">БИЧИЛ ХОРООЛОЛ МИНИ ДӨТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/81.jpg" class="card-img-top" alt="БИЧИЛ ХОРООЛОЛ МИНИ ДӨТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 6-р бичил хороолол, Castle lounge-н хойно, Дөт маркет дотор </p></div></div></a>

			<a class="branch-card" id="branch-94" href="/branches/94">
	<h5 class="card-title">ЭФЭС 10 ХОРООЛОЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/94.jpg" class="card-img-top" alt="ЭФЭС 10 ХОРООЛОЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 6-р хороо, 10-р хороолол, туслах замруу ороод, Эфэс супермаркетын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-98" href="/branches/98">
	<h5 class="card-title">ТҮМЭН ПЛАЗА САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/98.jpg" class="card-img-top" alt="ТҮМЭН ПЛАЗА САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
14- хороо, Ард-Аюушийн өргөн чөлөө-5, Шөлөндө-н доор, Түмэн плаза салбар дотор 
</p></div></div></a>

			<a class="branch-card" id="branch-99" href="/branches/99">
	<h5 class="card-title">ГУРВАН ГАЛ ЭМНЭЛЭГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/99.jpg" class="card-img-top" alt="ГУРВАН ГАЛ ЭМНЭЛЭГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-16:00
				<br>
								<strong>Бям-Ням:</strong>
					10:00-15:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 11-р хороо, Эх нялхасын хажууд, Гурван гал эмнэлэгийн урд</p></div></div></a>

			<a class="branch-card" id="branch-105" href="/branches/105">
	<h5 class="card-title">ГОЛДЕН ПАРК ОД</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/105.jpg" class="card-img-top" alt="ГОЛДЕН ПАРК ОД">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 10-р хороолол, Golden park хотхон, Од супермракет 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-116" href="/branches/116">
	<h5 class="card-title">4-Р ХОРООЛОЛ ТТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/116.jpg" class="card-img-top" alt="4-Р ХОРООЛОЛ ТТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 11-р хороо, 4-р хороолол, Энэбишийн гудамж, Билэг их дэлгүүрийн замын эсрэг талд, ОЧИР хотхон 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-118" href="/branches/118">
	<h5 class="card-title">ОРАНЖ МАРТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/118.jpg" class="card-img-top" alt="ОРАНЖ МАРТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 9-р хороо, 3, 4-р хорооллын эцэс, “ORANGE MART” супермаркетын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-122" href="/branches/122">
	<h5 class="card-title">ЗООС СУПЕРМАРКЕТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/122.jpg" class="card-img-top" alt="ЗООС СУПЕРМАРКЕТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, Нарын замын туслахаар ороод, Жаст ойл колонкын эсрэг талд, Зоос супермаркетын байран дээр </p></div></div></a>

			<a class="branch-card" id="branch-128" href="/branches/128">
	<h5 class="card-title">КОРАЛ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/128.jpg" class="card-img-top" alt="КОРАЛ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					11:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
КОРАЛ ТӨВ, 1 давхарт, Баянгол их дэлгүүрийн урд</p></div></div></a>

			<a class="branch-card" id="branch-132" href="/branches/132">
	<h5 class="card-title">СУПЕР ДЭЛГҮҮР МОДНЫ 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/132.jpg" class="card-img-top" alt="СУПЕР ДЭЛГҮҮР МОДНЫ 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД 4-р хороо, Модны 2-ын дунд зам дагуу, Гурван гал медийн хажууд, Супер дэлгүүрийн үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-137" href="/branches/137">
	<h5 class="card-title">ЭРДЭНЭС САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/137.jpg" class="card-img-top" alt="ЭРДЭНЭС САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
3-р хороолол, 15-р хороо, Л.Энэбишийн єргєн чєлєє, 1000 нэрийн барааний хажууд,  Эрдэнэс салбар дотор</p></div></div></a>

			<a class="branch-card" id="branch-140" href="/branches/140">
	<h5 class="card-title">АЛТАН ТӨГРӨГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/140.jpg" class="card-img-top" alt="АЛТАН ТӨГРӨГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 3-Р ХОРООЛОЛ АЛТАНТӨГРӨГ худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-148" href="/branches/148">
	<h5 class="card-title">АНАР СУПЕРМАРКЕТ ХАРХОРИН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/148.jpg" class="card-img-top" alt="АНАР СУПЕРМАРКЕТ ХАРХОРИН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 20-хороо, Энхтайваны гудамж, Эрэн хорооллын хойно, Төв зам дагуу, Анар супермаркетын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-192" href="/branches/192">
	<h5 class="card-title">БЭРС ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/192.jpg" class="card-img-top" alt="БЭРС ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянгол дүүрэг, 1-р хороо, Алтай хотхон, 9-р байр, Бэрс төв, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-218" href="/branches/218">
	<h5 class="card-title">Ю КЭЙ ТАУР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/218.jpg" class="card-img-top" alt="Ю КЭЙ ТАУР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, Хороолол, Парадоксын автобусны буудал, Юу Кэй тауэр үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-228" href="/branches/228">
	<h5 class="card-title">ИХ ТОЙРУУ 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/228.jpg" class="card-img-top" alt="ИХ ТОЙРУУ 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 9-р хороо, Дөлгөөн нуурын хойно Их тойруу худалдааны төвийн 1 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-240" href="/branches/240">
	<h5 class="card-title">ИМАРТ БАЯНГОЛ 3 ДАВХАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/240.jpg" class="card-img-top" alt="ИМАРТ БАЯНГОЛ 3 ДАВХАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 6-р хороо, И-март Баянгол 3 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-95800045" href="/branches/95800045">
	<h5 class="card-title">ЭВСЭГ ХК ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800045.jpg" class="card-img-top" alt="ЭВСЭГ ХК ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11343595
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Made in Mongolia</p></div></div></a>

			<a class="branch-card" id="branch-95800050" href="/branches/95800050">
	<h5 class="card-title">GOBI ( Discount 3% , 4% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800050.jpg" class="card-img-top" alt="GOBI ( Discount 3% , 4% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11320303
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Made in Mongolia</p></div></div></a>

			<a class="branch-card" id="branch-95800054" href="/branches/95800054">
	<h5 class="card-title">GOBI SAUNA ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800054.jpg" class="card-img-top" alt="GOBI SAUNA ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11301033
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Говь саун</p></div></div></a>

			<a class="branch-card" id="branch-95800069" href="/branches/95800069">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800069.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Эх нялхас урд</p></div></div></a>

			<a class="branch-card" id="branch-95800075" href="/branches/95800075">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800075.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГДүүргийн шүүх , Ганзам</p></div></div></a>

			<a class="branch-card" id="branch-95800084" href="/branches/95800084">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800084.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Ачлал их дэлгүүр замын урд</p></div></div></a>

			<a class="branch-card" id="branch-95800085" href="/branches/95800085">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800085.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 4 Хороолол, 7 Хороо, 90/3 </p></div></div></a>

			<a class="branch-card" id="branch-95800091" href="/branches/95800091">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800091.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД 10-р хороолол</p></div></div></a>

			<a class="branch-card" id="branch-95800097" href="/branches/95800097">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800097.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Нарны хороолол</p></div></div></a>

			<a class="branch-card" id="branch-95800099" href="/branches/95800099">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800099.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Төмөр зам арктай шар</p></div></div></a>

			<a class="branch-card" id="branch-95800100" href="/branches/95800100">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800100.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД 25-р эмийн сан</p></div></div></a>

			<a class="branch-card" id="branch-95800101" href="/branches/95800101">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800101.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД 7-р хороо Гэмтлийн эмнэлэг</p></div></div></a>

			<a class="branch-card" id="branch-95800124" href="/branches/95800124">
	<h5 class="card-title">ШҮР САЛОН ( Discount 5% , 8% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800124.jpg" class="card-img-top" alt="ШҮР САЛОН ( Discount 5% , 8% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70377300
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД Модны 2, White house</p></div></div></a>

			<a class="branch-card" id="branch-95800130" href="/branches/95800130">
	<h5 class="card-title">STRINGS NIGHT CLUB ( Discount 4% , 4% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800130.jpg" class="card-img-top" alt="STRINGS NIGHT CLUB ( Discount 4% , 4% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11365158
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД 18-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800132" href="/branches/95800132">
	<h5 class="card-title">TESCOMA SHOP ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800132.jpg" class="card-img-top" alt="TESCOMA SHOP ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11328286
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД Grand plaza</p></div></div></a>

			<a class="branch-card" id="branch-95800136" href="/branches/95800136">
	<h5 class="card-title">UNITED COLORS OF BENETTON (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800136.jpg" class="card-img-top" alt="UNITED COLORS OF BENETTON (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77065050
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД,15-р хороо, 3-р хороолол</p></div></div></a>

			<a class="branch-card" id="branch-15" href="/branches/15">
	<h5 class="card-title">ӨРГӨӨ САЛБАР ХОРООЛЛЫН ЭЦЭС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/15.jpg" class="card-img-top" alt="ӨРГӨӨ САЛБАР ХОРООЛЛЫН ЭЦЭС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
13-р хороо, Ард Аюушийн єргєн чєлєє гудамж, БСБ дэлгүүрийн баруун талд, Өргөө салбар дотор
</p></div></div></a>

			<a class="branch-card" id="branch-16" href="/branches/16">
	<h5 class="card-title">МАКС МООЛ 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/16.jpg" class="card-img-top" alt="МАКС МООЛ 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
16-р хороо, Гандан (16040), Энхтайваны өргөн чөлөө гудамж 35, Макс моол худалдааны төв, 1-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-58" href="/branches/58">
	<h5 class="card-title">ХАРХОРИН ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/58.jpg" class="card-img-top" alt="ХАРХОРИН ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 20-р хороо, Хархорин зах баруун урд тайлын байрны зүүн хаалга
</p></div></div></a>

			<a class="branch-card" id="branch-166" href="/branches/166">
	<h5 class="card-title">БАРС ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/166.jpg" class="card-img-top" alt="БАРС ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 3-р хороо, Барс зах, Нарны зам дагуу, Барс захын 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-176" href="/branches/176">
	<h5 class="card-title">ГРАНД САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/176.jpg" class="card-img-top" alt="ГРАНД САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баруун 4-н зам, Гранд плаза, 1-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-190" href="/branches/190">
	<h5 class="card-title">ХАРХОРИН ЗАХ В1 </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/190.jpg" class="card-img-top" alt="ХАРХОРИН ЗАХ В1 ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-16:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, Хар хорин худалдааны төв, В1 давхар
</p></div></div></a>

			<a class="branch-card" id="branch-200" href="/branches/200">
	<h5 class="card-title">ИМАРТ БАЯНГОЛ 1 ДАВХАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/200.jpg" class="card-img-top" alt="ИМАРТ БАЯНГОЛ 1 ДАВХАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 6-р хороо, И-март Баянгол 1 давхарт Баянгол салбарын үүдэнд
</p></div></div></a>

			<a class="branch-card" id="branch-203" href="/branches/203">
	<h5 class="card-title">БЛЮ СКАЙ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/203.jpg" class="card-img-top" alt="БЛЮ СКАЙ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СБД, 1-р хороо, Блю Скай Энхтайван салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-406" href="/branches/406">
	<h5 class="card-title">Богдхан салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/406.jpg" class="card-img-top" alt="Богдхан салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			341335
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7000 8975 /Мэдээллийн ажилтан/ &lt;br&gt;
344245 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 15-р хороо, Зайсангийн гудамж, Гэгээнтэн цогцолбор
</p></div></div></a>

			<a class="branch-card" id="branch-415" href="/branches/415">
	<h5 class="card-title">Хан-Уул салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/415.jpg" class="card-img-top" alt="Хан-Уул салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			342085 /Зээлийн мэргэжилтэн/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, Хан-Уул салбар</p></div></div></a>

			<a class="branch-card" id="branch-416" href="/branches/416">
	<h5 class="card-title">Нархан салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/416.jpg" class="card-img-top" alt="Нархан салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77110070 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70001170 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 15-р хороо, Махатма Гандигийн гудамж, Ханс Вилл хотхоны хойно</p></div></div></a>

			<a class="branch-card" id="branch-418" href="/branches/418">
	<h5 class="card-title">Дунд гол салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/418.jpg" class="card-img-top" alt="Дунд гол салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75052023 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75052024 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, үйлдвэрийн гудамж, Компорт плаза 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-427" href="/branches/427">
	<h5 class="card-title">Үйлдвэр салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/427.jpg" class="card-img-top" alt="Үйлдвэр салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70142086 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70142085 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 2-р хороо, Yйлдвэрийн 1742, Чингисийн єргєн чєлєє 20/1, БСБ мегамолл дэлгүүр 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-436" href="/branches/436">
	<h5 class="card-title">Ривер гарден салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/436.jpg" class="card-img-top" alt="Ривер гарден салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70001063 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70001062 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
УБ хот, ХУД, Их Монгол улсын гудамж, Их Монгол плаза, 2-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-440" href="/branches/440">
	<h5 class="card-title">Мишээл  салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/440.jpg" class="card-img-top" alt="Мишээл  салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75099955 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 2-р хороо, Чингисийн өргөн чөлөө,  Мишээл-2 худалдааны төв</p></div></div></a>

			<a class="branch-card" id="branch-444" href="/branches/444">
	<h5 class="card-title">Яармаг-Дрийм Плаза салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/444.jpg" class="card-img-top" alt="Яармаг-Дрийм Плаза салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7505-8222 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7505-8222 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Хан-уул дүүрэг, 4-р хороо, Наадамчдын гудамж, Арцат апартмент хотхон, 12-р блок 1441 тоот Дрийм плаза</p></div></div></a>

			<a class="branch-card" id="branch-446" href="/branches/446">
	<h5 class="card-title">Соёолж моол лайт хэсэг</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/446.jpg" class="card-img-top" alt="Соёолж моол лайт хэсэг">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:45
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7505-0640
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7505-0650<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 15-р хороо, Нарны зам 05/01, Соёолж худалдааны төвийн 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-451" href="/branches/451">
	<h5 class="card-title">Буянт-Ухаа салбар </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/451.jpg" class="card-img-top" alt="Буянт-Ухаа салбар ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77002257 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	77002267 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 5-р хороо, Яармаг 17110, Наадамчдын гудамж, Титан центр 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-474" href="/branches/474">
	<h5 class="card-title">Зайсан салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/474.jpg" class="card-img-top" alt="Зайсан салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			(976-11) 341149 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70101149 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 11-хороо, Зайсангийн тойруу 21/1 ММ проперти 1болон 2 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-803" href="/branches/803">
	<h5 class="card-title">Нарны гүүр салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/803.jpg" class="card-img-top" alt="Нарны гүүр салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7710 8222 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, ЗДТГ-ын зүүн хойно Булгат мөрөн ХХК-ийн байр, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-814" href="/branches/814">
	<h5 class="card-title">БИОКОМБИНАТ ТT</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/814.jpg" class="card-img-top" alt="БИОКОМБИНАТ ТT">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70492244 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 12-р хороо, 52-р байр, Био СӨХ</p></div></div></a>

			<a class="branch-card" id="branch-820" href="/branches/820">
	<h5 class="card-title">ОРГИЛ СТАР САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/820.jpg" class="card-img-top" alt="ОРГИЛ СТАР САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77118222 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	77008222 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 11-р хороо, Зайсангийн гудамж, Оргил стар таун 56-р байр, 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-822" href="/branches/822">
	<h5 class="card-title">Хүннү 2222 ТТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/822.jpg" class="card-img-top" alt="Хүннү 2222 ТТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			/Мэдээллийн ажилтан/ 7014 8222
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	/Зээлийн мэргэжилтэн/ 7015 8222<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 18-р хороо, Стадион оргил, Удирдлагын академийн гудамж, Ком 7</p></div></div></a>

			<a class="branch-card" id="branch-80301" href="/branches/80301">
	<h5 class="card-title">МИШЭЭЛ ТООЦООНЫ КАСС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/80301.jpg" class="card-img-top" alt="МИШЭЭЛ ТООЦООНЫ КАСС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					07:00-16:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7011 8222
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 2-р хороо, Чингисийн өргөн чөлөө, Мишээл барилгын их дэлгүүрийн Б-блок Нийслэлийн үйлчилгээний нэгдсэн төвийн Мишээл салбар</p></div></div></a>

			<a class="branch-card" id="branch-12" href="/branches/12">
	<h5 class="card-title">МАРКО 19-Н ҮЙЛЧИЛГЭЭНИЙ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/12.jpg" class="card-img-top" alt="МАРКО 19-Н ҮЙЛЧИЛГЭЭНИЙ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
2-р хороо, 19-р хорооллын үйлчилгээний төв дотор, Марко супер маркет 1 давхарт  </p></div></div></a>

			<a class="branch-card" id="branch-19" href="/branches/19">
	<h5 class="card-title">ДРИЙМ ПЛАЗА </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/19.jpg" class="card-img-top" alt="ДРИЙМ ПЛАЗА ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
4-р хороо, Наадамчдын гудамж, Ацарт апартмент хотхон, 12-р блок, 1441 тоот Дрийм плазагийн 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-35" href="/branches/35">
	<h5 class="card-title">ГОВЬ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/35.jpg" class="card-img-top" alt="ГОВЬ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, үйлдвэрийн гудамж, Дунд гол салбарын үүдэнд, Компорт плаза 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-55" href="/branches/55">
	<h5 class="card-title">ЗАЙСАН САРНАЙХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/55.jpg" class="card-img-top" alt="ЗАЙСАН САРНАЙХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 11-р хороо, Зайсан, Irish castle, Сарнайх супермаркет дотор</p></div></div></a>

			<a class="branch-card" id="branch-64" href="/branches/64">
	<h5 class="card-title">ХҮННҮ 2222 ТТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/64.jpg" class="card-img-top" alt="ХҮННҮ 2222 ТТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 18-р хороо, Стадион оргил,  Хүннү 2222 ТТ-ын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-74" href="/branches/74">
	<h5 class="card-title">БОСА ЯАРМАГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/74.jpg" class="card-img-top" alt="БОСА ЯАРМАГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Баа:</strong>
					10:00-20:00
				<br>
								<strong>Бям-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 6-р хороо, Нүхтийн 26-462, Яармагийн эцэс явах зам дагуу, CU дотор </p></div></div></a>

			<a class="branch-card" id="branch-80" href="/branches/80">
	<h5 class="card-title">ОРГИЛ СТАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/80.jpg" class="card-img-top" alt="ОРГИЛ СТАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 11-р хороо, Зайсангийн гудамж, Оргил стар таун 56-р байр, 1-р давхарт, Оргил стар салбарын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-92" href="/branches/92">
	<h5 class="card-title">ФЕРМЕР ЗАХ ЯАРМАГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/92.jpg" class="card-img-top" alt="ФЕРМЕР ЗАХ ЯАРМАГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, Яармагийн гүүр өнгөрөөд Туул кондоминум хотхоны доор 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-100" href="/branches/100">
	<h5 class="card-title">ЭРДЭНЭ СУПЕРМАРКЕТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/100.jpg" class="card-img-top" alt="ЭРДЭНЭ СУПЕРМАРКЕТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 25-р хороо, Буянт ухаа 1-р хороолол Эрдэнэ супермаркет</p></div></div></a>

			<a class="branch-card" id="branch-104" href="/branches/104">
	<h5 class="card-title">Баянхошуу нэг цэгийн үйлчилгээ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/104.jpg" class="card-img-top" alt="Баянхошуу нэг цэгийн үйлчилгээ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 9-р хороо, Баянхошуу нэг цэгийн үйлчилгээ</p></div></div></a>

			<a class="branch-card" id="branch-108" href="/branches/108">
	<h5 class="card-title">НОМИН ХАН ПЛАЗА </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/108.jpg" class="card-img-top" alt="НОМИН ХАН ПЛАЗА ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
16-р Хороо, Буянт-ухаа хороолол, /17120/ Наадамчдын зам гудамж, 103 тоот, Хан плаза төвийн байр, 1-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-130" href="/branches/130">
	<h5 class="card-title">ШУТИС МИС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/130.jpg" class="card-img-top" alt="ШУТИС МИС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, Механик Инженерийн сургууль, 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-131" href="/branches/131">
	<h5 class="card-title">ЗАЙСАН САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/131.jpg" class="card-img-top" alt="ЗАЙСАН САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
11-хороо, Зайсангийн тойруу 21/1 ММ проперти 1 болон 2 давхарт, Зайсан салбарын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-141" href="/branches/141">
	<h5 class="card-title">ВИВА СИТИ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/141.jpg" class="card-img-top" alt="ВИВА СИТИ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, ВИВА СИТИ, М эгнээ</p></div></div></a>

			<a class="branch-card" id="branch-171" href="/branches/171">
	<h5 class="card-title">ҮЙЛДВЭР САЛБАР БСБ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/171.jpg" class="card-img-top" alt="ҮЙЛДВЭР САЛБАР БСБ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
2-р хороо, Yйлдвэрийн 1742, Чингисийн єргєн чєлєє 20/1, БСБ мегамолл дэлгүүр 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-183" href="/branches/183">
	<h5 class="card-title">МОРЬТОН ЦОГЦОЛБОР ХАНУУЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/183.jpg" class="card-img-top" alt="МОРЬТОН ЦОГЦОЛБОР ХАНУУЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, 19-н автобусны буудлын урд талд сайн ломбардны урд талд </p></div></div></a>

			<a class="branch-card" id="branch-193" href="/branches/193">
	<h5 class="card-title">МИШЭЭЛ ТООЦООНЫ КАСС </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/193.jpg" class="card-img-top" alt="МИШЭЭЛ ТООЦООНЫ КАСС ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 2-р хороо, Чингисийн өргөн чөлөө, Мишээл барилгын их дэлгүүрийн Б-блок Нийслэлийн үйлчилгээний нэгдсэн төвийн Мишээл салбар
</p></div></div></a>

			<a class="branch-card" id="branch-196" href="/branches/196">
	<h5 class="card-title">РИВЕР ГАРДЕН 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/196.jpg" class="card-img-top" alt="РИВЕР ГАРДЕН 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Хан-Уул дүүрэг, 11-р хороо, Ривер гарден 2 хотхон, 406-р байр, Pizza Hut-н хажууд </p></div></div></a>

			<a class="branch-card" id="branch-207" href="/branches/207">
	<h5 class="card-title">ЗАЙСАН СТАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/207.jpg" class="card-img-top" alt="ЗАЙСАН СТАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, Гэгээнтэн кинотеартын замын урд талд, Tous les jours-н хажууд 
</p></div></div></a>

			<a class="branch-card" id="branch-210" href="/branches/210">
	<h5 class="card-title">CU ХҮННҮ 2222</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/210.jpg" class="card-img-top" alt="CU ХҮННҮ 2222">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Хүннү 2222 хороолол, 101-118 байр, 14 тоот CU-33 салбар </p></div></div></a>

			<a class="branch-card" id="branch-231" href="/branches/231">
	<h5 class="card-title">АТМ БИДНИЙ ЯАРМАГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/231.jpg" class="card-img-top" alt="АТМ БИДНИЙ ЯАРМАГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 6-р хороо, Нүхтийн 20-342а</p></div></div></a>

			<a class="branch-card" id="branch-234" href="/branches/234">
	<h5 class="card-title">ФҮҮД СИТИ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/234.jpg" class="card-img-top" alt="ФҮҮД СИТИ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 11-р хороо, Хүннү моллын замын эсрэг талд Фүүд сити худалдааны төвийн 3 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-237" href="/branches/237">
	<h5 class="card-title">АТМ НАРНЫ ГҮҮР САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/237.jpg" class="card-img-top" alt="АТМ НАРНЫ ГҮҮР САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, ЗДТГ-ын зүүн хойно Булгат мөрөн ХХК-ийн байр, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-95800034" href="/branches/95800034">
	<h5 class="card-title">AROMA SPA (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800034.jpg" class="card-img-top" alt="AROMA SPA (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77444040
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, Оргил шилтгээн</p></div></div></a>

			<a class="branch-card" id="branch-95800035" href="/branches/95800035">
	<h5 class="card-title">AROMA SPA (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800035.jpg" class="card-img-top" alt="AROMA SPA (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77444040
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, Соёл wellness</p></div></div></a>

			<a class="branch-card" id="branch-95800037" href="/branches/95800037">
	<h5 class="card-title">CHARMING BEAUTY SALON ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800037.jpg" class="card-img-top" alt="CHARMING BEAUTY SALON ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77339999
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, Белла виста</p></div></div></a>

			<a class="branch-card" id="branch-95800042" href="/branches/95800042">
	<h5 class="card-title">ЭВСЭГ ХК ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800042.jpg" class="card-img-top" alt="ЭВСЭГ ХК ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11343595
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Эвсэг төв байр</p></div></div></a>

			<a class="branch-card" id="branch-95800049" href="/branches/95800049">
	<h5 class="card-title">GOBI ( Discount 3% , 4% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800049.jpg" class="card-img-top" alt="GOBI ( Discount 3% , 4% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11320303
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Говь үйлдвэрийн байр</p></div></div></a>

			<a class="branch-card" id="branch-95800052" href="/branches/95800052">
	<h5 class="card-title">GOBI ( Discount 3% , 4% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800052.jpg" class="card-img-top" alt="GOBI ( Discount 3% , 4% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11320303
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Чингис хаан ОУНБ</p></div></div></a>

			<a class="branch-card" id="branch-95800057" href="/branches/95800057">
	<h5 class="card-title">ИНТЕРМЭД ЭМНЭЛЭГ ( Discount 3% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800057.jpg" class="card-img-top" alt="ИНТЕРМЭД ЭМНЭЛЭГ ( Discount 3% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77011111
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Интермэд эмнэлэг</p></div></div></a>

			<a class="branch-card" id="branch-95800073" href="/branches/95800073">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800073.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Номин агуулах</p></div></div></a>

			<a class="branch-card" id="branch-95800076" href="/branches/95800076">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800076.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Будда виста</p></div></div></a>

			<a class="branch-card" id="branch-95800087" href="/branches/95800087">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800087.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Оргил шилтгээн</p></div></div></a>

			<a class="branch-card" id="branch-95800103" href="/branches/95800103">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800103.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД 2-р хороо Орнаник зах</p></div></div></a>

			<a class="branch-card" id="branch-95800117" href="/branches/95800117">
	<h5 class="card-title">САРНАЙХ BEAUTY SALON ( Discount 5% ,  )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800117.jpg" class="card-img-top" alt="САРНАЙХ BEAUTY SALON ( Discount 5% ,  )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70111727
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Будда виста</p></div></div></a>

			<a class="branch-card" id="branch-95800118" href="/branches/95800118">
	<h5 class="card-title">САРНАЙХ SUPERMARKET ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800118.jpg" class="card-img-top" alt="САРНАЙХ SUPERMARKET ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70111727
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД 11-р хороо</p></div></div></a>

			<a class="branch-card" id="branch-95800119" href="/branches/95800119">
	<h5 class="card-title">САРНАЙХ SUPERMARKET ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800119.jpg" class="card-img-top" alt="САРНАЙХ SUPERMARKET ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70111727
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Хурд апартмент</p></div></div></a>

			<a class="branch-card" id="branch-95800120" href="/branches/95800120">
	<h5 class="card-title">САРНАЙХ SUPERMARKET ( Discount 5% , 5% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800120.jpg" class="card-img-top" alt="САРНАЙХ SUPERMARKET ( Discount 5% , 5% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70111727
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Будда виста</p></div></div></a>

			<a class="branch-card" id="branch-95800123" href="/branches/95800123">
	<h5 class="card-title">SEOUL OPTICS ( Discount 10% , 10% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800123.jpg" class="card-img-top" alt="SEOUL OPTICS ( Discount 10% , 10% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			91111288
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Гэгээнтэн</p></div></div></a>

			<a class="branch-card" id="branch-95800133" href="/branches/95800133">
	<h5 class="card-title">TESCOMA SHOP ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800133.jpg" class="card-img-top" alt="TESCOMA SHOP ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			11328286
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Зайсангийн тойрог</p></div></div></a>

			<a class="branch-card" id="branch-95800138" href="/branches/95800138">
	<h5 class="card-title">UNITED COLORS OF BENETTON (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800138.jpg" class="card-img-top" alt="UNITED COLORS OF BENETTON (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77075050
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД Оргил шилтгээн</p></div></div></a>

			<a class="branch-card" id="branch-95800139" href="/branches/95800139">
	<h5 class="card-title">UNITED COLORS OF BENETTON (Discount 3% , 5%)</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800139.jpg" class="card-img-top" alt="UNITED COLORS OF BENETTON (Discount 3% , 5%)">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			77085050
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 4-р хороо Хүннү Молл</p></div></div></a>

			<a class="branch-card" id="branch-18" href="/branches/18">
	<h5 class="card-title">РИВЕР ГАРДЕН САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/18.jpg" class="card-img-top" alt="РИВЕР ГАРДЕН САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
УБ хот, ХУД, 11-р хороо, Их Монгол Улсын гудамж, Их Монгол Плаза, 2-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-37" href="/branches/37">
	<h5 class="card-title">БОГДХАН САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/37.jpg" class="card-img-top" alt="БОГДХАН САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
15-р хороо, Зайсангийн гудамж, Гэгээнтэн цогцолбор, Богдхан салбарын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-60" href="/branches/60">
	<h5 class="card-title">РАПИД ЦЭНГЭЛДЭХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/60.jpg" class="card-img-top" alt="РАПИД ЦЭНГЭЛДЭХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 15-р хороо, Рапид харш, 8-р байр, Цэнгэлдэх супермаркетын 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-63" href="/branches/63">
	<h5 class="card-title">GS25 19 ХОРООЛОЛ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/63.jpg" class="card-img-top" alt="GS25 19 ХОРООЛОЛ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 3-р хороо, 19-р хороолол Нутгийн буян хотхон GS25
</p></div></div></a>

			<a class="branch-card" id="branch-82" href="/branches/82">
	<h5 class="card-title">ХАН УУЛ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/82.jpg" class="card-img-top" alt="ХАН УУЛ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
3-р хороо, MCS Анун төвийн байр, Хан-Уул салбарын үүдэнд 
</p></div></div></a>

			<a class="branch-card" id="branch-115" href="/branches/115">
	<h5 class="card-title">ЖИ ЭС 25 КИНГ ТАУР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/115.jpg" class="card-img-top" alt="ЖИ ЭС 25 КИНГ ТАУР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 17-р хороо, Кинг тауер хотхон 106-р байр</p></div></div></a>

			<a class="branch-card" id="branch-149" href="/branches/149">
	<h5 class="card-title">СИРКЛ-К БУДДА ВИСТА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/149.jpg" class="card-img-top" alt="СИРКЛ-К БУДДА ВИСТА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 11-р хороо, Будда виста хотхоны 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-156" href="/branches/156">
	<h5 class="card-title">ХҮННҮ МООЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/156.jpg" class="card-img-top" alt="ХҮННҮ МООЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					11:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 4-R ХОРОО, НААДАМЧДЫН ГУДАМЖ, ХҮННҮ худалдааны төвийн 1 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-160" href="/branches/160">
	<h5 class="card-title">МИШЭЭЛ СТРИЙТ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/160.jpg" class="card-img-top" alt="МИШЭЭЛ СТРИЙТ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 2-р хороо, Мишээл экспо, Мишээл вокинг стрийт 
</p></div></div></a>

			<a class="branch-card" id="branch-164" href="/branches/164">
	<h5 class="card-title">НААДАМ ЦЕНТР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/164.jpg" class="card-img-top" alt="НААДАМ ЦЕНТР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД 15-р хороо, Махатма Ганди-н гудамж, Наадам центрын 2 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-191" href="/branches/191">
	<h5 class="card-title">НАРХАН САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/191.jpg" class="card-img-top" alt="НАРХАН САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
15-р хороо, Махатма Гандигийн гудамж, Ханс Вилл хотхоны хойно /Нархан салбарын үүдэнд/
</p></div></div></a>

			<a class="branch-card" id="branch-202" href="/branches/202">
	<h5 class="card-title">ИМАРТ ХАН УУЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/202.jpg" class="card-img-top" alt="ИМАРТ ХАН УУЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-19:30
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 15-р хороо Чингисийн өргөн чөлөө, И-март худалдааны төв 2 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-212" href="/branches/212">
	<h5 class="card-title">Буянт ухаа салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/212.jpg" class="card-img-top" alt="Буянт ухаа салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
 5-р хороо, Яармаг 17110, Наадамчдын гудамж, Титан центр, 1-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-213" href="/branches/213">
	<h5 class="card-title">GS25 ДЭЭДСИЙН ӨРГӨӨ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/213.jpg" class="card-img-top" alt="GS25 ДЭЭДСИЙН ӨРГӨӨ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ХУД, 4-р хороо, Арцадын ам, Шинэ өргөө хотхон, GS25
</p></div></div></a>

			<a class="branch-card" id="branch-215" href="/branches/215">
	<h5 class="card-title">ЗАЙСАН САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/215.jpg" class="card-img-top" alt="ЗАЙСАН САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
11-хороо, Зайсангийн тойруу 21/1 ММ проперти 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-220" href="/branches/220">
	<h5 class="card-title">ОРГИЛ СТАР САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/220.jpg" class="card-img-top" alt="ОРГИЛ СТАР САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
11-р хороо, Зайсангийн гудамж, Оргил стар таун 56-р байр, 1-р давхарт /Оргил стар салбар дотор/
</p></div></div></a>

			<a class="branch-card" id="branch-412" href="/branches/412">
	<h5 class="card-title">Таван шар салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/412.jpg" class="card-img-top" alt="Таван шар салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям:</strong>
					11:00-15:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7018 0999 /зээлийн мэргэжилтэн/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7018 1299 /мэдээллийн ажилтан/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 21-р хороолол, БСБ таван шар Суперстор Дэлгvvрийн байр</p></div></div></a>

			<a class="branch-card" id="branch-424" href="/branches/424">
	<h5 class="card-title">Хархорин тооцооны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/424.jpg" class="card-img-top" alt="Хархорин тооцооны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					10:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70173966 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70172869 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
БГД, 1-р хороолол, 20-р хороо, Москвагийн гудамж, Хархорин худалдааны төвийн 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-437" href="/branches/437">
	<h5 class="card-title">Авто худалдааны салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/437.jpg" class="card-img-top" alt="Авто худалдааны салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					09:30-17:00
				<br>
								<strong>Мяг:</strong>
					Амарна
				<br>
								<strong>Лха-Бям:</strong>
					09:30-17:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75777437 - /Мэдээллийн ажилтан
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сонгинохайрхан дүүргийн 32-р хороо, Шинэ авто худалдааны цогцолбор</p></div></div></a>

			<a class="branch-card" id="branch-458" href="/branches/458">
	<h5 class="card-title">Гурвалжин салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/458.jpg" class="card-img-top" alt="Гурвалжин салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70180241 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70187547 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, Энхтайваны єргєн чєлєє 8/1, Гурвалжин салбар</p></div></div></a>

			<a class="branch-card" id="branch-468" href="/branches/468">
	<h5 class="card-title">Сонгинохайрхан салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/468.jpg" class="card-img-top" alt="Сонгинохайрхан салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7017 0091 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70170091 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 18-р хороо, хуучнаар 5-р авто баазын зvvн талд, Сансар vйлчилгээний тєв, 2-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-471" href="/branches/471">
	<h5 class="card-title">Цамбагарав салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/471.jpg" class="card-img-top" alt="Цамбагарав салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70003967 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70003968 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 1-р хороолол, 15-р хороо, Москвагийн гудамж, 44-р байрны 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-815" href="/branches/815">
	<h5 class="card-title">1-Р ХОРООЛОЛ TT</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/815.jpg" class="card-img-top" alt="1-Р ХОРООЛОЛ TT">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75075775 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75075885 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД,17-р хороо, UB vista үйлчилгээний төв, 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-80102" href="/branches/80102">
	<h5 class="card-title">Баянхошуу тооцооны касс</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/80102.jpg" class="card-img-top" alt="Баянхошуу тооцооны касс">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					07:00-16:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			19001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 8 дугаар хороо Баянцагааны 10-р гудамж Бизнес инкубатор Баянхошуу дэд төв </p></div></div></a>

			<a class="branch-card" id="branch-14" href="/branches/14">
	<h5 class="card-title">МИНИЙ ДЭЛГҮҮР 21</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/14.jpg" class="card-img-top" alt="МИНИЙ ДЭЛГҮҮР 21">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
19-р хороо, 21-р хороолол миний дэлгүүр 21, төв зам дагуу, 1 давхарт, кассын хажууд</p></div></div></a>

			<a class="branch-card" id="branch-36" href="/branches/36">
	<h5 class="card-title">САНСАР СОНГИНОХАЙРХАН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/36.jpg" class="card-img-top" alt="САНСАР СОНГИНОХАЙРХАН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
18-р хороо, хуучнаар 5-р авто баазын зvvн талд, Сансар vйлчилгээний тєв, 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-65" href="/branches/65">
	<h5 class="card-title">ГУРВАЛЖИН САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/65.jpg" class="card-img-top" alt="ГУРВАЛЖИН САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Энхтайваны єргєн чєлєє 8/1, Саппоро автобусны буудлын хойно, Гурвалжин салбар дотор</p></div></div></a>

			<a class="branch-card" id="branch-84" href="/branches/84">
	<h5 class="card-title">1-Р ХОРООЛОЛ ТТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/84.jpg" class="card-img-top" alt="1-Р ХОРООЛОЛ ТТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 17-р хороо, UB vista үйлчилгээний төв, 1 давхар, 1-р хороолол ТТ-ын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-88" href="/branches/88">
	<h5 class="card-title">НОМИН МОСКВА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/88.jpg" class="card-img-top" alt="НОМИН МОСКВА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, Москвагийн гудамж, Хөрс худалдааны төвийн 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-89" href="/branches/89">
	<h5 class="card-title">БОСА БАЯНХОШУУ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/89.jpg" class="card-img-top" alt="БОСА БАЯНХОШУУ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-23:00
				<br>
								<strong>Бям-Ням:</strong>
					09:30-20:30
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 10-р хороо, Баянхошууны шинэ эцсийн буудал, М Мартын 1 давхарт </p></div></div></a>

			<a class="branch-card" id="branch-134" href="/branches/134">
	<h5 class="card-title">ЦАМБАГАРАВ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/134.jpg" class="card-img-top" alt="ЦАМБАГАРАВ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
1-р хороолол, 15-р хороо, Москвагийн гудамж, 44-р байр, 1-р давхар, Цамбагарав салбарын үүдэнд </p></div></div></a>

			<a class="branch-card" id="branch-147" href="/branches/147">
	<h5 class="card-title">БАЯНХОШУУ ЭРҮҮЛ МЭНДИЙН ТӨВ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/147.jpg" class="card-img-top" alt="БАЯНХОШУУ ЭРҮҮЛ МЭНДИЙН ТӨВ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, Баянхошуу эрүүл мэндийн төвийн 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-150" href="/branches/150">
	<h5 class="card-title">СХД ЭРҮҮЛ МЭНДИЙН НЭГДЭЛ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/150.jpg" class="card-img-top" alt="СХД ЭРҮҮЛ МЭНДИЙН НЭГДЭЛ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 19-р хороо, 21-р хороолол, Сонгинохайрхан нэгдсэн эмнэлэг /Цамбагаравын эмнэлэг/
</p></div></div></a>

			<a class="branch-card" id="branch-161" href="/branches/161">
	<h5 class="card-title">СОНГИНОХАЙРХАН ЗАХ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/161.jpg" class="card-img-top" alt="СОНГИНОХАЙРХАН ЗАХ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 6-р хороо, Сонгино-Хайрхан захын 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-163" href="/branches/163">
	<h5 class="card-title">ЭНХЖИН ХУДАЛДААНЫ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/163.jpg" class="card-img-top" alt="ЭНХЖИН ХУДАЛДААНЫ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 20-р хороо, Энхжин худалдааны төв, 1 давхарт  </p></div></div></a>

			<a class="branch-card" id="branch-225" href="/branches/225">
	<h5 class="card-title">НОМИН 1-Р ХОРООЛОЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/225.jpg" class="card-img-top" alt="НОМИН 1-Р ХОРООЛОЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сонгинохайрхан дүүрэг, 14-р хороо, 23-р байрны урд Өнөр плаза, Номин супермаркет, 1 давхарт
</p></div></div></a>

			<a class="branch-card" id="branch-226" href="/branches/226">
	<h5 class="card-title">ЭРЧИМ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/226.jpg" class="card-img-top" alt="ЭРЧИМ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сонгинохайрхан дүүрэг, 23-р хороо, 34-р байрны баруун хойд дэнж, Эрчим худалдааны төв, 1 давхарт</p></div></div></a>

			<a class="branch-card" id="branch-232" href="/branches/232">
	<h5 class="card-title">АТМ ВЭЛЛМАРТ ТОВЧОО</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/232.jpg" class="card-img-top" alt="АТМ ВЭЛЛМАРТ ТОВЧОО">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 20-р хороо, Wellmart сүлжээ дэлгүүр /22н товчооны замд/</p></div></div></a>

			<a class="branch-card" id="branch-238" href="/branches/238">
	<h5 class="card-title">АТМ СХД НЭГДСЭН ЭМНЭЛЭГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/238.jpg" class="card-img-top" alt="АТМ СХД НЭГДСЭН ЭМНЭЛЭГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 19-р хороо, 21-р хороолол, Сонгинохайрхан нэгдсэн эмнэлэгийн 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-239" href="/branches/239">
	<h5 class="card-title">Шинэ Сандэй худалдааны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/239.jpg" class="card-img-top" alt="Шинэ Сандэй худалдааны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД, 5-р хороо, Хархорин захын хжууд, шинэ сандэй худалдааны төвийн В1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-95800079" href="/branches/95800079">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800079.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД Таван шар</p></div></div></a>

			<a class="branch-card" id="branch-95800090" href="/branches/95800090">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800090.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД Хархорин</p></div></div></a>

			<a class="branch-card" id="branch-95800093" href="/branches/95800093">
	<h5 class="card-title">МОНОС ЭМИЙН САН ( Discount 3% , 3% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800093.jpg" class="card-img-top" alt="МОНОС ЭМИЙН САН ( Discount 3% , 3% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			1800-1883
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД Баянхошууны эцэс</p></div></div></a>

			<a class="branch-card" id="branch-95800126" href="/branches/95800126">
	<h5 class="card-title">ШҮР САЛОН ( Discount 5% , 8% )</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/95800126.jpg" class="card-img-top" alt="ШҮР САЛОН ( Discount 5% , 8% )">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70377300
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
СХД Титэм плаза</p></div></div></a>

			<a class="branch-card" id="branch-2" href="/branches/2">
	<h5 class="card-title">МИНИЙ ДЭЛГҮҮР САППОРО</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/2.jpg" class="card-img-top" alt="МИНИЙ ДЭЛГҮҮР САППОРО">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Саппоро доторх Миний дэлгүүр дотор ороо 1 давхарын баруун хойно 
</p></div></div></a>

			<a class="branch-card" id="branch-11" href="/branches/11">
	<h5 class="card-title">5 ШАР БСБ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/11.jpg" class="card-img-top" alt="5 ШАР БСБ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
21-р хороолол, БСБ таван шар Суперстор Дэлгvvрийн байр, 1 давхарт 
</p></div></div></a>

			<a class="branch-card" id="branch-201" href="/branches/201">
	<h5 class="card-title">ШИНЭ НИСЭХ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/201.jpg" class="card-img-top" alt="ШИНЭ НИСЭХ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Төв аймаг, Сэргэлэн сум, Чингис Хаан Олон Улсын нисэх буудлын 2 дугаар давхар
</p></div></div></a>

			<a class="branch-card" id="branch-5800001" href="/branches/5800001">
	<h5 class="card-title">ДОРНОД ЧОЙБАЛСАН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5800001.jpg" class="card-img-top" alt="ДОРНОД ЧОЙБАЛСАН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
7-р баг Чадангууд цогцолбор</p></div></div></a>

			<a class="branch-card" id="branch-5800002" href="/branches/5800002">
	<h5 class="card-title">ДОРНОД НАРЛАГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5800002.jpg" class="card-img-top" alt="ДОРНОД НАРЛАГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорнод аймаг, Хэрлэн сум 6-р баг Нарлаг супермаркет</p></div></div></a>

			<a class="branch-card" id="branch-5800003" href="/branches/5800003">
	<h5 class="card-title">ДОРНОД СИТИ ЦЕНТР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5800003.jpg" class="card-img-top" alt="ДОРНОД СИТИ ЦЕНТР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
6-р баг "ДБЭХС" ХК-ийн "Хэрэглэгчдэд үйлчлэх төв"</p></div></div></a>

			<a class="branch-card" id="branch-401" href="/branches/401">
	<h5 class="card-title">Дорнод салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/401.jpg" class="card-img-top" alt="Дорнод салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7058 3680  /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7058 3624 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорнод аймаг, Хэрлэн сум 7-р баг, Монголбанктай байрны баруун талд</p></div></div></a>

			<a class="branch-card" id="branch-422" href="/branches/422">
	<h5 class="card-title">Хэрлэн тооцооны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/422.jpg" class="card-img-top" alt="Хэрлэн тооцооны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					10:00-18:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7058 3625 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7058 3626 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорнод аймаг,&nbsp;Хэрлэн сум 9-р баг, Сити центр худалдааны тєвийн 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-5800004" href="/branches/5800004">
	<h5 class="card-title">ДОРНОД ТАНА ХУДАЛДААНЫ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5800004.jpg" class="card-img-top" alt="ДОРНОД ТАНА ХУДАЛДААНЫ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					09:00-18:00
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорнод аймаг Хэрлэн сум 6-р баг СМУ-н хашаанд-1</p></div></div></a>

			<a class="branch-card" id="branch-430" href="/branches/430">
	<h5 class="card-title">Шинэ нисэх салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/430.jpg" class="card-img-top" alt="Шинэ нисэх салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			71287971 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	71287972/Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Төв баймаг, Сэргэлэн сум, Чингис Хаан Олон Улсын нисэх буудлын 1 болон 2 дугаар давхар</p></div></div></a>

			<a class="branch-card" id="branch-455" href="/branches/455">
	<h5 class="card-title">Зүүн хараа салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/455.jpg" class="card-img-top" alt="Зүүн хараа салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7036 7623 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7036 7523 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сэлэнгэ аймаг, Мандал сум, 3-р баг, Буян тахь худалдааны тєв, 1, 2-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-3647001" href="/branches/3647001">
	<h5 class="card-title">ЗҮҮНХАРАА ТӨМӨР ЗАМЫН БУУДАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3647001.jpg" class="card-img-top" alt="ЗҮҮНХАРАА ТӨМӨР ЗАМЫН БУУДАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Зүүн хараа</p></div></div></a>

			<a class="branch-card" id="branch-3647002" href="/branches/3647002">
	<h5 class="card-title">ЗҮҮНХАРАА САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3647002.jpg" class="card-img-top" alt="ЗҮҮНХАРАА САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сэлэнгэ аймаг, Мандал сум, 3-р баг, Буян тахь худалдааны тєв, 1, 2-р давхар
</p></div></div></a>

			<a class="branch-card" id="branch-469" href="/branches/469">
	<h5 class="card-title">Хөтөл салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/469.jpg" class="card-img-top" alt="Хөтөл салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7036 8496 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сэлэнгэ аймаг, Сайхан сум, Гавшгай 2-р баг</p></div></div></a>

			<a class="branch-card" id="branch-3651001" href="/branches/3651001">
	<h5 class="card-title">ХӨТӨЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3651001.jpg" class="card-img-top" alt="ХӨТӨЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан Хөтөл</p></div></div></a>

			<a class="branch-card" id="branch-454" href="/branches/454">
	<h5 class="card-title">Замын-Vvд салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/454.jpg" class="card-img-top" alt="Замын-Vvд салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			43578 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	43605 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорноговь аймаг, Замын-Yүд сум, 1-р баг, Тєв талбай</p></div></div></a>

			<a class="branch-card" id="branch-5200003" href="/branches/5200003">
	<h5 class="card-title">ЗАМЫН-ҮҮД БАЯНТҮШЛЭГ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5200003.jpg" class="card-img-top" alt="ЗАМЫН-ҮҮД БАЯНТҮШЛЭГ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорноговь аймаг, Замын-Үүд сум, 1-р баг, Төв талбай, Баянтүшлэг супермаркетийн 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-408" href="/branches/408">
	<h5 class="card-title">Дорноговь салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/408.jpg" class="card-img-top" alt="Дорноговь салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7052 2298 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7052 2258 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорноговь аймаг, Сайншанд сум, 3-р баг, Монгол банкны байр</p></div></div></a>

			<a class="branch-card" id="branch-465" href="/branches/465">
	<h5 class="card-title">Дорноговь ТТөв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/465.jpg" class="card-img-top" alt="Дорноговь ТТөв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			02522 42611 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	42442 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорноговь аймаг, Сайншанд сум, 4-р баг</p></div></div></a>

			<a class="branch-card" id="branch-5200001" href="/branches/5200001">
	<h5 class="card-title">ЗАМЫН-ҮҮД</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5200001.jpg" class="card-img-top" alt="ЗАМЫН-ҮҮД">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Замын үүд төмөр зам</p></div></div></a>

			<a class="branch-card" id="branch-5200004" href="/branches/5200004">
	<h5 class="card-title">САЙНШАНД ТӨМӨР ЗАМ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5200004.jpg" class="card-img-top" alt="САЙНШАНД ТӨМӨР ЗАМ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сайншанд шуудан</p></div></div></a>

			<a class="branch-card" id="branch-5200005" href="/branches/5200005">
	<h5 class="card-title">ЗАМЫН-ҮҮД ТӨВ САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5200005.jpg" class="card-img-top" alt="ЗАМЫН-ҮҮД ТӨВ САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорноговь аймаг, Замын-Yүд сум, 1-р баг, Тєв талбай
</p></div></div></a>

			<a class="branch-card" id="branch-5200006" href="/branches/5200006">
	<h5 class="card-title">САЙНШАНД ШИНЭ ҮЙЛЧИЛГЭЭНИЙ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5200006.jpg" class="card-img-top" alt="САЙНШАНД ШИНЭ ҮЙЛЧИЛГЭЭНИЙ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дорноговь, Сайншанд, Шинэ үйлчилгээний төв”</p></div></div></a>

			<a class="branch-card" id="branch-5200002" href="/branches/5200002">
	<h5 class="card-title">САЙНШАНД ШУУДАНГИЙН САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5200002.jpg" class="card-img-top" alt="САЙНШАНД ШУУДАНГИЙН САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Сайншанд төмөр зам
</p></div></div></a>

			<a class="branch-card" id="branch-3700012" href="/branches/3700012">
	<h5 class="card-title">ECRM ДАРХАН ЛАЙТ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700012.jpg" class="card-img-top" alt="ECRM ДАРХАН ЛАЙТ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан-Уул аймаг 7-р баг “Дархан зах”-ын нэг давхар</p></div></div></a>

			<a class="branch-card" id="branch-403" href="/branches/403">
	<h5 class="card-title">Дархан салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/403.jpg" class="card-img-top" alt="Дархан салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7037 0378
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7037 0379 /Мэдээллийн ажилтан/ &lt;br&gt;
7037 0377 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан уул аймаг, 12 дугаар баг, 6 дугаар хороолол “Найрамдал” талбайд</p></div></div></a>

			<a class="branch-card" id="branch-467" href="/branches/467">
	<h5 class="card-title">ДАРХАН ЛАЙТ ХЭСЭГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/467.jpg" class="card-img-top" alt="ДАРХАН ЛАЙТ ХЭСЭГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Бям:</strong>
					09:00-17:45
				<br>
								<strong>Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			75050609 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	75050608 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан-уул аймаг, Дархан сум, Дархан захын Алтансагс үйлчилгээний төвийн 1 давхар</p></div></div></a>

			<a class="branch-card" id="branch-476" href="/branches/476">
	<h5 class="card-title">Хуучин Дархан ТТөв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/476.jpg" class="card-img-top" alt="Хуучин Дархан ТТөв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70374247
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70373726<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан-Уул аймаг, Дархан сум, 8-р баг, Микро хороолол</p></div></div></a>

			<a class="branch-card" id="branch-3700001" href="/branches/3700001">
	<h5 class="card-title">ДАРХАН-2 ТӨМӨР ЗАМ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700001.jpg" class="card-img-top" alt="ДАРХАН-2 ТӨМӨР ЗАМ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан төмөрзам</p></div></div></a>

			<a class="branch-card" id="branch-3700003" href="/branches/3700003">
	<h5 class="card-title">ДАРХАН ГРИЙН МАГНОЛИА</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700003.jpg" class="card-img-top" alt="ДАРХАН ГРИЙН МАГНОЛИА">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан Грийн Магнолиа</p></div></div></a>

			<a class="branch-card" id="branch-3700004" href="/branches/3700004">
	<h5 class="card-title">ДАРХАН ИХ ДЭЛГҮҮР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700004.jpg" class="card-img-top" alt="ДАРХАН ИХ ДЭЛГҮҮР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:30-22:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан их дэлгүүр</p></div></div></a>

			<a class="branch-card" id="branch-3700005" href="/branches/3700005">
	<h5 class="card-title">ДАРХАН ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700005.jpg" class="card-img-top" alt="ДАРХАН ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-21:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан зах</p></div></div></a>

			<a class="branch-card" id="branch-3700006" href="/branches/3700006">
	<h5 class="card-title">ДАРХАН НАНДИН СУПЕРМАРКЕТ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700006.jpg" class="card-img-top" alt="ДАРХАН НАНДИН СУПЕРМАРКЕТ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан уул аймаг, Дархан сум, 14-р баг, Парк тоун 2 хотхон, 102-А байр</p></div></div></a>

			<a class="branch-card" id="branch-3700007" href="/branches/3700007">
	<h5 class="card-title">ДАРХАН НЭГДСЭН ЭМНЭЛЭГ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700007.jpg" class="card-img-top" alt="ДАРХАН НЭГДСЭН ЭМНЭЛЭГ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					08:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан эмнэлэг </p></div></div></a>

			<a class="branch-card" id="branch-3700008" href="/branches/3700008">
	<h5 class="card-title">ДАРХАН ХУУЧИН САЛБАР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700008.jpg" class="card-img-top" alt="ДАРХАН ХУУЧИН САЛБАР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан-Уул аймаг, Дархан сум, 8-р баг, Микро хороолол
</p></div></div></a>

			<a class="branch-card" id="branch-3700009" href="/branches/3700009">
	<h5 class="card-title">ДАРХАН КОМФОРТ ЗОЧИД БУУДАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700009.jpg" class="card-img-top" alt="ДАРХАН КОМФОРТ ЗОЧИД БУУДАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан Комфорт буудал</p></div></div></a>

			<a class="branch-card" id="branch-3700011" href="/branches/3700011">
	<h5 class="card-title">ДАРХАН ГЯЛС СУПЕРМАРКЕТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700011.jpg" class="card-img-top" alt="ДАРХАН ГЯЛС СУПЕРМАРКЕТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан-Уул аймаг Дархан сум 5-р баг Гялс супермаркет</p></div></div></a>

			<a class="branch-card" id="branch-3700002" href="/branches/3700002">
	<h5 class="card-title">ДАРХАН-1 ОУХТ ХОЛБОО</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700002.jpg" class="card-img-top" alt="ДАРХАН-1 ОУХТ ХОЛБОО">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					09:00-18:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан худалдааны төв</p></div></div></a>

			<a class="branch-card" id="branch-3700010" href="/branches/3700010">
	<h5 class="card-title">ДАРХАН ТЭЭВЭР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700010.jpg" class="card-img-top" alt="ДАРХАН ТЭЭВЭР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав:</strong>
					Амарна
				<br>
								<strong>Мяг-Ням:</strong>
					10:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ДАРХАН ТЭЭВЭР</p></div></div></a>

			<a class="branch-card" id="branch-3700013" href="/branches/3700013">
	<h5 class="card-title">ДАРХАН БАРИЛГЫН ЗАХ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3700013.jpg" class="card-img-top" alt="ДАРХАН БАРИЛГЫН ЗАХ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-19:30
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Дархан салбар 2</p></div></div></a>

			<a class="branch-card" id="branch-443" href="/branches/443">
	<h5 class="card-title">Цогтцэций тооцооны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/443.jpg" class="card-img-top" alt="Цогтцэций тооцооны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			70535513 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	70535512 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Өмнөговь аймаг, Цогтцэций сум, 4-р баг</p></div></div></a>

			<a class="branch-card" id="branch-5300004" href="/branches/5300004">
	<h5 class="card-title">ӨМНӨГОВЬ ЦОГТЦЭЦИЙ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5300004.jpg" class="card-img-top" alt="ӨМНӨГОВЬ ЦОГТЦЭЦИЙ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Цогтцэций сум, 4-р баг, Камель төв </p></div></div></a>

			<a class="branch-card" id="branch-414" href="/branches/414">
	<h5 class="card-title">Өмнөговь салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/414.jpg" class="card-img-top" alt="Өмнөговь салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7053 4242 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7053 4343 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Өмнөговь аймаг, Даланзадгад сум, 3-р баг</p></div></div></a>

			<a class="branch-card" id="branch-5300001" href="/branches/5300001">
	<h5 class="card-title">ӨМНӨГОВЬ СОЁМБО</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5300001.jpg" class="card-img-top" alt="ӨМНӨГОВЬ СОЁМБО">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Өмнөговь номин</p></div></div></a>

			<a class="branch-card" id="branch-5300002" href="/branches/5300002">
	<h5 class="card-title">ӨМНӨГОВЬ ГАНДИРС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5300002.jpg" class="card-img-top" alt="ӨМНӨГОВЬ ГАНДИРС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-16:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Өмнөговь, Даланзадгад, 3-р баг, Далан, 11-р цэцэрлэгийн зүүн талд Гандирс худалдааны төв</p></div></div></a>

			<a class="branch-card" id="branch-5300003" href="/branches/5300003">
	<h5 class="card-title">ӨМНӨГОВЬ САЛБАР </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/5300003.jpg" class="card-img-top" alt="ӨМНӨГОВЬ САЛБАР ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Өмнөговь аймаг,Даланзадгад сум, 3-р баг , Гандирс цамхаг
</p></div></div></a>

			<a class="branch-card" id="branch-407" href="/branches/407">
	<h5 class="card-title">Эрдэнэт салбар</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/407.jpg" class="card-img-top" alt="Эрдэнэт салбар">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7035 5135 Мэдээллийн ажилтан
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7035 8077 Зээлийн мэргэжилтэн<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Орхон аймаг, Баян-Өндөр сум, Хүрэнбулаг баг, Эрдэнэт салбар</p></div></div></a>

			<a class="branch-card" id="branch-466" href="/branches/466">
	<h5 class="card-title">ОРХОН ТООЦООНЫ ТӨВ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/466.jpg" class="card-img-top" alt="ОРХОН ТООЦООНЫ ТӨВ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:30-17:30
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7035 7647 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7035 7647 /Зээлийн ажилтан/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Орхон аймаг, Баян-Өндөр сум, Согоот баг, 6-р хороолол, Пирамид төвийн зүүн талын барилгын 1-р давхарт</p></div></div></a>

			<a class="branch-card" id="branch-3500001" href="/branches/3500001">
	<h5 class="card-title">ЭРДЭНЭТ АЧИТ ХОЛДИНГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500001.jpg" class="card-img-top" alt="ЭРДЭНЭТ АЧИТ ХОЛДИНГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-19:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Ачит холдинг</p></div></div></a>

			<a class="branch-card" id="branch-3500002" href="/branches/3500002">
	<h5 class="card-title">ЭРДЭНЭТ ӨРГӨӨ-4</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500002.jpg" class="card-img-top" alt="ЭРДЭНЭТ ӨРГӨӨ-4">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт салбар</p></div></div></a>

			<a class="branch-card" id="branch-3500003" href="/branches/3500003">
	<h5 class="card-title">ЭРДЭНЭТ ТӨГӨЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500003.jpg" class="card-img-top" alt="ЭРДЭНЭТ ТӨГӨЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					08:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт төгөл их дэлгүүр</p></div></div></a>

			<a class="branch-card" id="branch-3500004" href="/branches/3500004">
	<h5 class="card-title">ЭРДЭНЭТ САЛБАР 3 CASH</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500004.jpg" class="card-img-top" alt="ЭРДЭНЭТ САЛБАР 3 CASH">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт касс</p></div></div></a>

			<a class="branch-card" id="branch-3500005" href="/branches/3500005">
	<h5 class="card-title">ЭРДЭНЭТ ХАЙ МАРТ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500005.jpg" class="card-img-top" alt="ЭРДЭНЭТ ХАЙ МАРТ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт их дэлгүүр</p></div></div></a>

			<a class="branch-card" id="branch-3500007" href="/branches/3500007">
	<h5 class="card-title">ЭРДЭНЭТ БАЯН ШОППИНГ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500007.jpg" class="card-img-top" alt="ЭРДЭНЭТ БАЯН ШОППИНГ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт баян худалдааны төв</p></div></div></a>

			<a class="branch-card" id="branch-3500008" href="/branches/3500008">
	<h5 class="card-title">ЭРДЭНЭТ ТӨВ САЛБАР 1</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500008.jpg" class="card-img-top" alt="ЭРДЭНЭТ ТӨВ САЛБАР 1">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт салбар</p></div></div></a>

			<a class="branch-card" id="branch-3500009" href="/branches/3500009">
	<h5 class="card-title">ЭРДЭНЭТ ХИВС</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500009.jpg" class="card-img-top" alt="ЭРДЭНЭТ ХИВС">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-20:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт хивс</p></div></div></a>

			<a class="branch-card" id="branch-3500010" href="/branches/3500010">
	<h5 class="card-title">ЭРДЭНЭТ ИХ ДЭЛГҮҮР</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500010.jpg" class="card-img-top" alt="ЭРДЭНЭТ ИХ ДЭЛГҮҮР">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					10:00-23:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт грави</p></div></div></a>

			<a class="branch-card" id="branch-3500011" href="/branches/3500011">
	<h5 class="card-title">ЭРДЭНЭТ СУВИЛАЛ</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500011.jpg" class="card-img-top" alt="ЭРДЭНЭТ СУВИЛАЛ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт Сувилал</p></div></div></a>

			<a class="branch-card" id="branch-3500012" href="/branches/3500012">
	<h5 class="card-title">ЭРДЭНЭТ БИБИ-ОД</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500012.jpg" class="card-img-top" alt="ЭРДЭНЭТ БИБИ-ОД">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					09:00-00:00
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
ЭРДЭНЭТ САЛБАР</p></div></div></a>

			<a class="branch-card" id="branch-3500006" href="/branches/3500006">
	<h5 class="card-title">ЭРДЭНЭТ ОРХОН</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500006.jpg" class="card-img-top" alt="ЭРДЭНЭТ ОРХОН">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт орхон</p></div></div></a>

			<a class="branch-card" id="branch-3500013" href="/branches/3500013">
	<h5 class="card-title">ЭРДЭНЭТ САЛБАР 2</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/3500013.jpg" class="card-img-top" alt="ЭРДЭНЭТ САЛБАР 2">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Ням:</strong>
					00:01-23:59
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Эрдэнэт салбар</p></div></div></a>

			<a class="branch-card" id="branch-445" href="/branches/445">
	<h5 class="card-title">Баянхонгор тооцооны төв</h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/445.jpg" class="card-img-top" alt="Баянхонгор тооцооны төв">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			7509 - 1119 /Мэдээллийн ажилтан/
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	7509 - 1117 /Зээлийн мэргэжилтэн/<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянхонгор аймаг, Баянхонгор сум, 1-р баг, Номгон нисэхийн 1-т байрлах Мазаалай зочид буудлын 1-р давхар</p></div></div></a>

			<a class="branch-card" id="branch-6400001" href="/branches/6400001">
	<h5 class="card-title">БАЯНХОНГОР ТООЦООНЫ ТӨВ </h5>
	<div class="card">
		<img src="https://www.tdbm.mn/sites/default/files/branches/6400001.jpg" class="card-img-top" alt="БАЯНХОНГОР ТООЦООНЫ ТӨВ ">
		<div class="card-body">
			<p class="card-text">
				<i class="fa-light fa-clock" aria-hidden="true"></i>
									<strong>Дав-Баа:</strong>
					09:00-17:00
				<br>
								<strong>Бям-Ням:</strong>
					Амарна
				<br>
					</p>
		<p class="card-text">
			<i class="fa-light fa-phone-volume" aria-hidden="true"></i>
			<strong>Мэдээллийн ажилтан::
			</strong>
			18001977
		</p>
	<br>
	<strong>Зээлийн мэргэжилтэн::
	</strong>
	<br><p></p><p class="card-text">
<i class="fa-light fa-location-dot" aria-hidden="true"></i>
Баянхонгор аймаг,  Баянхонгор сум, 1-р баг, Номгон нисэхийн 1-т байрлах Мазаалай зочид буудлын 1-р давхар </p></div></div></a>

	</div>

				</div>"""

# h = markdownify.markdownify(html, heading_style="UNDERLINED ") 

# print(h)


from bs4 import BeautifulSoup

def parse_branches(html):
    soup = BeautifulSoup(html, 'html.parser')
    branches = []
    
    for branch in soup.select(".branch-card"):
        name = branch.select_one(".card-title").text.strip()
        hours = branch.select(".card-text")[0].get_text(" ", strip=True)
        phone_info = branch.select(".card-text")[1].get_text(" ", strip=True) if len(branch.select(".card-text")) > 1 else ""
        location = branch.select(".card-text")[-1].get_text(" ", strip=True)
        
        branches.append({
            "name": name,
            "hours": hours,
            "phone_info": phone_info,
            "location": location
        })
    
    return branches

def write_to_md(branches, filename="branches.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Салбрын жагсаалт\n")
        for branch in branches:
            f.write(f"## {branch['name']}\n")
            f.write(f"**Ажиллах цаг:** {branch['hours']}\n")
            f.write(f"**холбоо барих:** {branch['phone_info']}\n")
            f.write(f"**Хаяг:** {branch['location']}\n")

# Example usage
# html = """(your HTML content here)"""
branches = parse_branches(html)
write_to_md(branches)
