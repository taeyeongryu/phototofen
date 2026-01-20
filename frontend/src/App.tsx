import Layout from './components/Layout'

function App() {
  return (
    <Layout>
      <div className="bg-white p-8 rounded-lg shadow-sm border border-gray-200">
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Welcome</h2>
        <p className="text-gray-600">
          Ready to convert your chess puzzle photos? Upload an image to get started.
        </p>
        {/* We will add the ImageUpload component here in the next phase */}
        <div className="mt-8 p-12 border-2 border-dashed border-gray-300 rounded-lg text-center text-gray-400">
          Upload component will be here.
        </div>
      </div>
    </Layout>
  )
}

export default App
