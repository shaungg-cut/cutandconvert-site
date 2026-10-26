PATH = "index.html"
ACTIVE = "home"
TITLE = "Cut &amp; Convert | Google Ads &amp; YouTube Ads Agency in San Diego"
DESC = "Cut & Convert is a San Diego Google Ads and YouTube Ads agency driving DTC sales, local leads and performance creative."

BODY = f"""
  <section class="hero">
    <div class="wrap">
      <div class="hero-copy">
        <span class="pill">Google Ads &amp; YouTube Ads · San Diego</span>
        <h1 class="rotator-head">
          <span class="sr-only">We drive DTC sales, leads and performance creative.</span>
          <span aria-hidden="true">We drive</span>
          <span class="rotator" aria-hidden="true">
            <span class="rotator-word is-active">DTC sales.</span>
            <span class="rotator-word">leads.</span>
            <span class="rotator-word">performance creative.</span>
          </span>
        </h1>
        <p class="lede">Big-brand Google and YouTube media buying plus a filmmaker's eye. Built for ecommerce brands and local businesses ready to grow.</p>
        <div class="actions">
          <a class="btn btn-coral" href="#contact">Book a free audit</a>
          <a class="btn btn-outline" href="#paths">Explore services</a>
        </div>
      </div>
      <div class="hero-art" aria-hidden="true"><span class="amp">&amp;</span></div>
    </div>
  </section>

  <section class="proof" aria-label="Experience">
    <div class="wrap">
      <div><p class="stat">$500M+</p><p class="muted">in ad spend managed</p></div>
      <div><p class="stat">9+ years</p><p class="muted">running Google and YouTube ads</p></div>
      <div><p class="stat">$40K → $300K</p><p class="muted">daily spend scaled, CPA held</p></div>
      <div><p class="stat">14+ years</p><p class="muted">behind the camera</p></div>
    </div>
  </section>

{MARQUEE}

  <section class="section" id="paths">
    <div class="wrap">
      <div class="section-head">
        <h2>Pick your path</h2>
        <p>Three ways we work together. Most clients start with one and add the others.</p>
      </div>
      <div class="cards">

        <a class="card card-link" href="/ecommerce/">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 4h2l2.4 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 8H6.2"/><circle cx="10" cy="20" r="1.2"/><circle cx="17" cy="20" r="1.2"/></svg>
          <h3>Ecommerce</h3>
          <p class="muted">Profitable, full-funnel growth on Search, Shopping, Performance Max and YouTube.</p>
          <span class="more">Drive DTC sales →</span>
        </a>

        <a class="card card-link" href="/local/">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>
          <h3>Local Business</h3>
          <p class="muted">Get found when people in your area search for what you do, and turn those searches into calls.</p>
          <span class="more">Drive local leads →</span>
        </a>

        <a class="card card-link" href="/youtube-creative/">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10.5 21 7.5v9l-5-3"/></svg>
          <h3>YouTube Creative</h3>
          <p class="muted">We re-edit the videos you already have into performance creative built for YouTube.</p>
          <span class="more">Make your videos sell →</span>
        </a>

      </div>
    </div>
  </section>

  <section class="section how">
    <div class="wrap">
      <h2>How it works</h2>
      <div class="steps">
        <div class="step"><span class="num">01</span><h3>Audit</h3><p>A free look at your Google Ads account, tracking and creative. You get a clear list of what to fix first.</p></div>
        <div class="step"><span class="num">02</span><h3>Cut</h3><p>We rebuild the campaigns and the creative together, so your ads and videos tell one story.</p></div>
        <div class="step"><span class="num">03</span><h3>Convert</h3><p>Test, measure what is truly incremental, and scale what works. Weekly reporting in plain English.</p></div>
      </div>
    </div>
  </section>

  <section class="section results" id="work">
    <div class="wrap">
      <div class="section-head"><h2>Results</h2></div>
      <div class="cards">
        <div class="result">
          <span class="label">Telehealth brand · Google Search + Demand Gen</span>
          <p class="big">$40K to $300K+ per day</p>
          <p class="muted">Daily spend scaled more than 7x without CPA degradation.</p>
        </div>
        <div class="result">
          <span class="label">Subscription supplement brand · Google Ads</span>
          <p class="big">$500 to $30K per day</p>
          <p class="muted">Grew into a brand later acquired by Unilever.</p>
        </div>
      </div>
    </div>
  </section>

{cta("Let's see what's leaving money on the table.", "Free 30-minute audit of your Google and YouTube ads.", "Free%20audit%20request")}"""

SCRIPTS = """
<script>
(function () {
  var words = document.querySelectorAll('.rotator-word');
  if (!words.length) return;
  var i = 0;
  setInterval(function () {
    words[i].classList.remove('is-active');
    words[i].classList.add('is-leaving');
    var prev = words[i];
    setTimeout(function () { prev.classList.remove('is-leaving'); }, 600);
    i = (i + 1) % words.length;
    words[i].classList.add('is-active');
  }, 2600);
})();
</script>"""
