import { ConnectButton } from '@rainbow-me/rainbowkit';

export default function App() {
  return (
    <div className="min-h-screen bg-black text-white p-8">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-2xl font-bold">Burna Boy Token</h1>
        <ConnectButton />
      </header>

      <main className="space-y-6">
        <div className="bg-gray-900 p-6 rounded-lg">
          <h2 className="text-xl font-semibold">Token Stats</h2>
          <p>$BURNA / WETH Price: $0.01272</p>
          <p>Market Cap: $127.07M</p>
          <p>Holders: 6</p>
        </div>

        <div className="bg-gray-900 p-6 rounded-lg">
          <h2 className="text-xl font-semibold mb-4">Swap $BURNA</h2>
          <iframe
            src="https://app.uniswap.org/#/swap?outputCurrency=0x00B...6AAE"
            height="660px"
            width="100%"
            style={{ border: '0', marginTop: '1rem', borderRadius: '10px' }}
          />
        </div>
      </main>
    </div>
  );
}