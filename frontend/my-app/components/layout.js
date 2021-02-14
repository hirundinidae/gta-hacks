import Header from './header'
import Head from 'next/head'

// add types of layouts (home, article, profile, etc.)
// in Layout arguments and use if statements to identify

export default function Layout({ children }) {
  return (
    <div className="layout">
      <Head>
        <title>Resourca</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Header />
      <main>
        { children }
      </main>
    </div>
  )
}