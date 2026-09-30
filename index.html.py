<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Gojo Bot | Free Discord Bot</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, sans-serif;
            background: #070711;
            color: white;
            overflow-x: hidden;
        }

        /* BACKGROUND */
        body::before {
            content: "";
            position: fixed;
            width: 500px;
            height: 500px;
            background: #6f35ff;
            filter: blur(180px);
            opacity: 0.18;
            top: -200px;
            left: -150px;
            z-index: -1;
        }

        body::after {
            content: "";
            position: fixed;
            width: 450px;
            height: 450px;
            background: #00aaff;
            filter: blur(180px);
            opacity: 0.12;
            bottom: -200px;
            right: -150px;
            z-index: -1;
        }

        /* NAVBAR */

        nav {
            position: sticky;
            top: 0;
            z-index: 100;
            padding: 18px 25px;
            background: rgba(7, 7, 17, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid #29233d;
        }

        .nav-content {
            max-width: 1100px;
            margin: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 22px;
            font-weight: bold;
            color: #b98cff;
        }

        nav a {
            color: #ccc;
            text-decoration: none;
            margin-left: 18px;
            font-size: 14px;
        }

        nav a:hover {
            color: white;
        }

        /* HERO */

        .hero {
            min-height: 90vh;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 70px 20px;
        }

        .hero-content {
            max-width: 800px;
        }

        .gojo-icon {
            font-size: 80px;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }

            50% {
                transform: translateY(-12px);
            }
        }

        h1 {
            font-size: clamp(45px, 10vw, 85px);
            margin: 10px 0;
            background: linear-gradient(90deg, #ffffff, #b78cff, #6c5cff);
            -webkit-background-clip: text;
            color: transparent;
        }

        .subtitle {
            color: #bdbdbd;
            font-size: 20px;
            margin-bottom: 22px;
        }

        /* FREE BADGE */

        .free {
            display: inline-block;
            padding: 9px 18px;
            border-radius: 50px;
            background: #182d20;
            border: 1px solid #36d978;
            color: #5cff91;
            font-weight: bold;
            margin-bottom: 30px;
            box-shadow: 0 0 20px rgba(54, 217, 120, 0.15);
        }

        /* BUTTONS */

        .buttons {
            display: flex;
            flex-direction: column;
            gap: 14px;
            max-width: 380px;
            margin: auto;
        }

        .button {
            display: block;
            padding: 17px 20px;
            border-radius: 13px;
            text-decoration: none;
            color: white;
            font-weight: bold;
            font-size: 17px;
            background: linear-gradient(135deg, #6d35d9, #4d43d9);
            box-shadow: 0 0 25px rgba(111, 53, 255, 0.25);
            transition: 0.25s;
        }

        .button:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 0 35px rgba(139, 92, 255, 0.5);
        }

        .button.free-button {
            background: linear-gradient(135deg, #7138e8, #9a61ff);
        }

        /* SECTIONS */

        section.content {
            max-width: 1000px;
            margin: auto;
            padding: 80px 20px;
            text-align: center;
        }

        section.content h2 {
            font-size: 35px;
            color: #c39cff;
            margin-bottom: 15px;
        }

        section.content > p {
            color: #aaa;
            line-height: 1.7;
            max-width: 700px;
            margin: auto;
        }

        /* CARDS */

        .cards {
            margin-top: 35px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 18px;
        }

        .card {
            background: rgba(20, 18, 35, 0.8);
            border: 1px solid #30264d;
            border-radius: 18px;
            padding: 28px 20px;
            transition: 0.25s;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: #754cff;
            box-shadow: 0 0 25px rgba(117, 76, 255, 0.15);
        }

        .card .emoji {
            font-size: 38px;
            margin-bottom: 15px;
        }

        .card h3 {
            color: #e0d1ff;
            margin-bottom: 10px;
        }

        .card p {
            color: #999;
            line-height: 1.5;
        }

        /* SPECIAL COMMUNITY BOX */

        .community {
            margin-top: 35px;
            padding: 35px 20px;
            border-radius: 20px;
            background: linear-gradient(
                135deg,
                rgba(90, 44, 170, 0.2),
                rgba(20, 20, 50, 0.8)
            );
            border: 1px solid #49316e;
        }

        /* FOOTER */

        footer {
            text-align: center;
            padding: 35px 20px;
            border-top: 1px solid #222;
            color: #777;
        }

        footer strong {
            color: #b98cff;
        }

        /* MOBILE */

        @media (max-width: 600px) {

            nav a {
                display: none;
            }

            .hero {
                min-height: 85vh;
                padding-top: 50px;
            }

            .gojo-icon {
                font-size: 65px;
            }

            .subtitle {
                font-size: 17px;
            }

            section.content {
                padding: 60px 18px;
            }
        }
    </style>
</head>

<body>

    <!-- NAVIGATION -->

    <nav>
        <div class="nav-content">
            <div class="logo">🤞 GOJO</div>

            <div>
                <a href="#features">Features</a>
                <a href="#support">Support</a>
                <a href="#community">Community</a>
            </div>
        </div>
    </nav>


    <!-- HERO -->

    <div class="hero">

        <div class="hero-content">

            <div class="gojo-icon">🤞</div>

            <h1>GOJO BOT</h1>

            <p class="subtitle">
                Your powerful Discord companion ⚡
            </p>

            <div class="free">
                🆓 100% FREE TO USE
            </div>

            <div class="buttons">

                <!-- BOT INVITE -->

                <a
                    class="button free-button"
                    href="https://discord.com/oauth2/authorize?client_id=1554544895815983155&permissions=8&integration_type=0&scope=applications.commands+bot"
                    target="_blank">
                    🤖 Add Gojo to Discord
                </a>

                <!-- SUPPORT SERVER -->

                <a
                    class="button"
                    href="https://discord.gg/EFpZRuETvV"
                    target="_blank">
                    🛠️ Gojo Support Server
                </a>

                <!-- MAIN SERVER -->

                <a
                    class="button"
                    href="https://discord.gg/9AUumhBmS6"
                    target="_blank">
                    🎮 Blox Fruits + Steal an Egg
                </a>

            </div>

        </div>

    </div>


    <!-- ABOUT -->

    <section class="content">

        <h2>🤖 What is Gojo?</h2>

        <p>
            Gojo is a Discord bot created to bring useful tools,
            automatic responses and fun features to Discord servers.
        </p>

    </section>


    <!-- FEATURES -->

    <section class="content" id="features">

        <h2>⚡ Features</h2>

        <p>
            Useful features designed to make your Discord server
            easier and more fun to manage.
        </p>

        <div class="cards">

            <div class="card">
                <div class="emoji">🤖</div>
                <h3>AI Auto Responder</h3>
                <p>
                    Gojo can automatically respond to members'
                    questions and messages.
                </p>
            </div>

            <div class="card">
                <div class="emoji">🛡️</div>
                <h3>Server Tools</h3>
                <p>
                    Useful tools to help manage and organize
                    your Discord community.
                </p>
            </div>

            <div class="card">
                <div class="emoji">⚡</div>
                <h3>Easy Commands</h3>
                <p>
                    Simple commands that members can use
                    inside your server.
                </p>
            </div>

            <div class="card">
                <div class="emoji">🎮</div>
                <h3>Gaming Community</h3>
                <p>
                    Connect with players who enjoy Blox Fruits
                    and Steal an Egg.
                </p>
            </div>

        </div>

    </section>


    <!-- SUPPORT -->

    <section class="content" id="support">

        <h2>🛠️ Need Help?</h2>

        <p>
            Need help with Gojo, want to report a bug,
            or have a feature suggestion?
        </p>

        <br>

        <a
            class="button"
            href="https://discord.gg/EFpZRuETvV"
            target="_blank">
            💬 Join Gojo Support
        </a>

    </section>


    <!-- COMMUNITY -->

    <section class="content" id="community">

        <h2>🎮 My Gaming Community</h2>

        <div class="community">

            <p>
                Join my official Blox Fruits + Steal an Egg
                Discord community!
            </p>

            <br>

            <a
                class="button"
                href="https://discord.gg/9AUumhBmS6"
                target="_blank">
                🚀 Join the Community
            </a>

        </div>

    </section>


    <!-- CREATOR -->

    <section class="content">

        <h2>👑 Creator</h2>

        <p>
            Gojo Bot was created by <strong>Aarav</strong>.
        </p>

    </section>


    <!-- FOOTER -->

    <footer>

        <p>
            © 2026 <strong>Gojo Bot</strong>
        </p>

        <p>
            🆓 Free to use • Made with ❤️
        </p>

    </footer>

</body>
</html>