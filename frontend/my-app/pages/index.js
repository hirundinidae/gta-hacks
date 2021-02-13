import Head from 'next/head'

import Layout from '../components/layout'

export default function Home() {
  return (
    <Layout>
      <Head>
        <title>Our App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <section className="hero">
        <div className="wrapper">
          <div className="content">
            <h1>
              Welcome to SiteName
            </h1>
            <div className="svg">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
              </svg>
            </div>
          </div>
        </div>
      </section>
      <section>
        
      </section>
    </Layout>
  )
}
