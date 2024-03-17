import { Navigation } from "../components/Navbar";
import { Tool } from "../components/Tool";

const user = {
    name: 'Tom Cook',
    email: 'tom@example.com',
    imageUrl:
      'https://media.licdn.com/dms/image/C4E03AQG8QvOozTMhVg/profile-displayphoto-shrink_200_200/0/1658075330700?e=1716422400&v=beta&t=sUM_3Ms0oW1Y2gy3dhTu2qX35R1RKQwrsGDMF2FW6iM',
  }
  const navigation = [
    { name: 'Dashboard', href: '#', current: true },
    { name: 'Demo', href: 'demo', current: false },
    { name: 'Examples', href: 'examples', current: false },
  ]
  const userNavigation = [
    { name: 'Your Profile', href: '#' },
    { name: 'Settings', href: '#' },
    { name: 'Sign out', href: '#' },
  ]

function Home() {
    return (
        <div className="min-h-full">
            <div className="bg-gray-800 pb-32">>
                <Navigation navigation={navigation} userNavigation={userNavigation} user={user} />
                <header className="py-10">
                    <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
                    <h1 className="text-3xl font-bold tracking-tight text-white">Dashboard</h1>
                    </div>
                </header>
            </div>
            <main className="-mt-32">
                <Tool />
            </main>
        </div>
    );
}

export default Home;