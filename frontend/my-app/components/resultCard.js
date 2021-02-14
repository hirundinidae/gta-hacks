export default function ResultCard({ name }) {
  return (
    <div className="lg:w-72 lg:h-auto lg:p-8 lg:rounded-2xl lg:shadow-xl">
      <h1 className="lg:text-left lg:text-lg">{ name }</h1>
    </div>
  )
}