import { ConnectButton } from '@rainbow-me/rainbowkit';
import { useEffect, useState } from 'react';
import axios from 'axios';

export default function BurnaDApp() {
  const [price, setPrice] = useState(null);

  useEffect(() => {
    async function fetchPrice() {
      try {
        const response = await axios.get(
          'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
        );
        const ethPrice = response.data.ethereum.usd;
        const burnaPrice = (ethPrice * 0.0000075).toFixed(5);
        setPrice(burnaPrice);
      } catch (err) {
        console.error("Error fetching price", err);
      }
    }

    fetchPrice();
  }, []);

  return (
    <div className="min-h-screen bg-black text-white p-8 bg-[url('/logo-watermark.png')] bg-center bg-no-repeat bg-cover">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Burna Boy Token ($BURNA)</h1>
        <ConnectButton />
      </header>

      <main className="space-y-8">
        <section className="bg-gray-900 p-6 rounded-lg shadow-xl">
          <h2 className="text-2xl font-semibold mb-2">Live Token Stats</h2>
          <p className="text-lg">Price: <strong>${price || 'Loading...'} USD</strong></p>
          <p>Market Cap: <span className="text-green-400">$127.07M</span></p>
          <p>Total Holders: <span className="text-green-400">6</span></p>
        </section>

        <section className="bg-gray-900 p-6 rounded-lg shadow-xl">
          <h2 className="text-2xl font-semibold mb-4">Swap $BURNA on Uniswap</h2>
          <iframe
            src="https://app.uniswap.org/#/swap?outputCurrency=0x00B...6AAE"
            height="660px"
            width="100%"
            style={{ border: '0', borderRadius: '10px' }}
            title="Uniswap Swap"
          />
        </section>

        <section className="bg-gray-900 p-6 rounded-lg shadow-xl">
          <h2 className="text-2xl font-semibold mb-2">About $BURNA</h2>
          <p>
            $BURNA is the official fan-powered token inspired by Burna Boy, created to bring music, culture, and Web3 together.
            Use $BURNA to swap, earn, and engage in exclusive community activities.
          </p>
        </section>
      </main>

      <footer className="mt-12 text-center text-gray-400">
        &copy; {new Date().getFullYear()} Burna Boy Token. All rights reserved.
      </footer>
    </div>
  );
}
