import Head from 'next/head'

import Layout from '../components/layout'
import Button from '../components/button'

export default function Home() {
  return (
    <Layout>
      <Head>
        <title>Our App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <section>
        <div className="wrapper">
          <div className="content">
            <h1>Hello!</h1>
            <p>Welcome to our app.</p>
            <Button>Get Started  →</Button>
          </div>
        </div>
      </section>
    </Layout>
  )
}
