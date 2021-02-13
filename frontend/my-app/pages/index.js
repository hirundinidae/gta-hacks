import Head from 'next/head'

import Layout from '../components/layout'
import { siteTitle } from '../components/header'
import TeamCard from '../components/teamCard'

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
              Welcome to { siteTitle }
            </h1>
            <div className="svg">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
              </svg>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div className="wrapper">
          <div className="content">
            <h1>Education reinvented.</h1>
            <p>{ siteTitle } is a database of course materials made for students and teachers alike.</p>
            <button>Get Started</button>
          </div>
        </div>
      </section>
      <section>
        <div className="wrapper">
          <div className="content">
            <h1>Meet our Team</h1>
            <div className="team-card-container">
              <TeamCard name="Diana" title="Backend Engineer" colour="bg-blue-600" />
              <TeamCard name="Prasun" title="Frontend Developer" colour="bg-red-600" />
              <TeamCard name="Stephen" title="Backend Engineer" colour="bg-yellow-400" />
              <TeamCard name="Neyha" title="UI Designer" colour="bg-green-600" />
            </div>
          </div>
        </div>
      </section>
    </Layout>
  )
}
