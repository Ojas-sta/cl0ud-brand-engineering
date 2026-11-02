<template>
  <div class="cl0ud-credit-card">
    <div class="cl0ud-credit-header">
      <span class="cl0ud-powered-text">POWERED BY <strong class="cl0ud-brand-text">cl0ud</strong></span>
      <svg class="cl0ud-mini-icon" viewBox="0 0 608 408" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path stroke="#38BDF8" stroke-width="32" stroke-linejoin="round" fill="none" d="M 309.8 1.5 c -23.8 3.0 -45.7 11.0 -65.4 23.8 -16.7 10.8 -31.5 24.8 -42.8 40.3 l -5.5 7.6 -5.1 -1.4 c -7.4 -2.1 -26.8 -2.8 -36.7 -1.3 -39.4 5.7 -70.9 32.3 -83.0 70.0 l -2.7 8.5 -8.8 6.2 c -38.8 27.0 -59.7 66.9 -59.7 113.8 -0.1 22.0 4.3 40.6 14.2 61.0 6.8 14.0 15.6 25.8 28.0 37.8 19.9 19.2 41.2 30.5 68.4 36.4 6.9 1.5 13.4 1.8 40.7 1.8 35.1 -0.0 39.2 -0.4 55.4 -5.7 34.2 -11.0 63.0 -34.9 96.1 -79.7 37.2 -50.3 44.9 -60.4 55.3 -72.2 22.3 -25.5 45.9 -42.4 72.3 -51.7 11.5 -4.1 22.8 -5.6 35.3 -4.9 11.9 0.7 19.5 2.6 29.1 7.2 19.6 9.5 33.7 26.4 40.7 48.5 2.0 6.4 2.3 9.5 2.3 21.5 -0.1 13.2 -0.3 14.5 -3.5 23.9 -7.1 20.9 -21.6 37.0 -41.5 46.2 -14.9 6.9 -13.3 6.7 -83.5 7.2 l -63.5 0.4 -13.5 18.0 c -7.4 9.9 -18.2 23.4 -23.8 30.0 l -10.4 11.9 90.9 -0.4 c 89.0 -0.3 91.0 -0.4 99.3 -2.5 19.3 -4.8 31.9 -10.5 49.1 -22.0 47.4 -31.7 69.8 -91.1 55.6 -147.2 -12.3 -48.2 -49.8 -85.9 -98.0 -98.4 l -9.0 -2.4 -2.3 -9.8 c -2.9 -12.7 -7.1 -24.0 -13.9 -37.3 -22.0 -42.6 -62.3 -73.3 -109.0 -83.1 -11.5 -2.4 -39.4 -3.5 -51.1 -2.0 z m 39.2 60.4 c 29.0 6.2 55.4 26.2 68.1 51.9 4.8 9.7 9.7 23.8 8.6 24.7 -0.5 0.3 -3.3 1.4 -6.3 2.5 -28.5 9.6 -52.0 25.4 -80.5 53.9 -19.7 19.8 -28.6 30.4 -57.0 68.1 -22.1 29.4 -29.2 38.0 -41.2 49.6 -20.2 19.6 -39.7 29.9 -62.9 33.0 -5.7 0.7 -16.9 1.0 -31.9 0.6 -19.6 -0.4 -24.1 -0.8 -30.5 -2.6 -45.2 -13.1 -68.8 -61.6 -51.0 -104.5 9.5 -22.8 26.7 -37.9 51.2 -45.0 l 8.3 -2.4 0.6 -12.8 c 0.6 -15.4 2.9 -23.2 9.1 -31.5 7.6 -10.2 19.2 -16.8 32.3 -18.4 7.2 -0.8 7.8 -0.1 6.4 7.1 -0.8 4.1 -1.3 29.3 -1.6 82.2 l -0.4 76.4 3.3 -0.7 c 16.0 -3.5 33.6 -17.1 49.7 -38.7 l 7.2 -9.8 -0.7 -42.2 c -0.4 -28.7 -0.3 -45.4 0.5 -51.9 3.2 -28.0 16.3 -52.6 37.0 -69.1 13.7 -11.0 32.0 -19.2 48.6 -21.8 7.8 -1.2 24.2 -0.5 33.1 1.4 z" />
      </svg>
    </div>

    <div class="cl0ud-divider"></div>

    <div class="cl0ud-credit-body">
      <div class="cl0ud-role">{{ role }}</div>
      <div class="cl0ud-founder-name">{{ engineer }}</div>
      <div class="cl0ud-disciplines">{{ tagline }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  role: {
    type: String,
    default: "CO-ENGINEERED BY"
  },
  engineer: {
    type: String,
    default: "OJAS SINGH"
  },
  tagline: {
    type: String,
    default: "Engineering • Innovation • Development"
  }
});
</script>

<style scoped>
.cl0ud-credit-card {
  box-sizing: border-box;
  width: 100%;
  max-width: 820px;
  background-color: #000000;
  border: 1px solid #27272a;
  border-radius: 20px;
  padding: 22px 28px;
  margin: 1.5rem auto;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  color: #ffffff;
  text-align: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
}

.cl0ud-credit-header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding-bottom: 18px;
}

.cl0ud-powered-text {
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0.08em;
  color: #f4f4f5;
  text-transform: uppercase;
}

.cl0ud-brand-text {
  font-weight: 700;
  letter-spacing: 0.02em;
}

.cl0ud-mini-icon {
  width: 24px;
  height: 18px;
  vertical-align: middle;
}

.cl0ud-divider {
  height: 1px;
  background-color: #27272a;
  width: 100%;
  margin: 0 auto;
}

.cl0ud-credit-body {
  padding-top: 22px;
  padding-bottom: 8px;
}

.cl0ud-role {
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 0.14em;
  color: #a1a1aa;
  margin-bottom: 8px;
}

.cl0ud-founder-name {
  font-size: 26px;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #ffffff;
  margin-bottom: 8px;
}

.cl0ud-disciplines {
  font-size: 13.5px;
  font-weight: 400;
  color: #a1a1aa;
  letter-spacing: 0.02em;
}
</style>
