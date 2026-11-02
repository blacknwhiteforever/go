document.addEventListener("DOMContentLoaded", function() {
    const modalHTML = `
        <div class="global-modal-overlay" id="globalAdModal">
            <div class="global-modal-box">
                <h2>Enjoying BlacknWhite?</h2>
                <p>Please wait for the ad to finish. The page will unlock automatically.</p>
                <div class="global-modal-ad-space">
                    <script type="text/javascript">
                      atOptions = { 'key' : '23d98862449809c04e4c9daf55c3d963', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {} };
                    <\/script>
                    <script type="text/javascript" src="https://bauval.org/22/23d98862449809c04e4c9daf55c3d963"><\/script>
                </div>
                <div class="global-countdown-text">Unlocking in <span id="globalTimer">10</span> seconds...</div>
            </div>
        </div>
        <style>
            .global-modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.9); backdrop-filter: blur(8px); display: none; justify-content: center; align-items: center; z-index: 99999; padding: 20px; }
            .global-modal-overlay.active { display: flex; }
            .global-modal-box { background: #fff; padding: 30px 20px; text-align: center; max-width: 400px; width: 100%; box-shadow: 0 20px 50px rgba(0,0,0,0.5); border-radius: 12px; }
            .global-modal-box h2 { font-family: 'Playfair Display', serif; font-size: 1.6rem; margin-bottom: 10px; color: #111; }
            .global-modal-box p { font-size: 0.95rem; color: #666; margin-bottom: 15px; }
            .global-countdown-text { font-size: 1.1rem; font-weight: 600; color: #000; margin-top: 15px; }
            .global-countdown-text span { color: #ff0000; }
            .global-modal-ad-space { display: flex; justify-content: center; margin: 15px 0; min-height: 250px; }
        </style>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    const modal = document.getElementById("globalAdModal");
    const timerElement = document.getElementById("globalTimer");
    let isModalOpen = false;

    function showAdModal() {
        if (isModalOpen) return;
        isModalOpen = true;
        modal.classList.add("active");
        document.body.style.overflow = 'hidden'; 

        let timeLeft = 10;
        timerElement.innerText = timeLeft;

        let countdownInterval = setInterval(function() {
            timeLeft--;
            timerElement.innerText = timeLeft;
            if (timeLeft <= 0) {
                clearInterval(countdownInterval);
                modal.classList.remove("active");
                document.body.style.overflow = 'auto'; 
                isModalOpen = false;
                localStorage.setItem('bnw_last_ad_time', Date.now());
            }
        }, 1000);
    }

    const COOLDOWN = 1200000; // 20 minutes
    let lastAdTime = localStorage.getItem('bnw_last_ad_time');

    if (!lastAdTime) {
        setTimeout(showAdModal, 15000);
    } else {
        let timePassed = Date.now() - parseInt(lastAdTime);
        if (timePassed >= COOLDOWN) {
            setTimeout(showAdModal, 15000);
        } else {
            let timeLeft = COOLDOWN - timePassed;
            setTimeout(() => {
                if (document.visibilityState === 'visible' && !isModalOpen) {
                    showAdModal();
                }
            }, timeLeft);
        }
    }

    setInterval(() => {
        if (document.visibilityState === 'visible' && !isModalOpen) {
            let lastTime = localStorage.getItem('bnw_last_ad_time');
            if (!lastTime || Date.now() - parseInt(lastTime) >= COOLDOWN) {
                showAdModal();
            }
        }
    }, 60000); 
});
