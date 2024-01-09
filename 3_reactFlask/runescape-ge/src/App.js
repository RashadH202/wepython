import React, {useState, useEffect} from 'react';

function App() {
  const [data, setData] = useState({
    current:{
      price: '',
      trend: ''
    }, 
    day180:{
      price: '',
      trend: ''
    }, 
    day30:{
      price: '',
      trend: ''
    }, 
    day90:{
      price: '',
      trend: ''
    }, 
    description:'', 
    icon:'', 
    icon_large:'', 
    indexOf:'', 
    members:'', 
    name:'', 
    today:{
      price: '',
      trend: ''
    }, 
    type:'',
    typeIcon:''})
    

  useEffect(()=>{
    fetch('http://127.0.0.1:5000/')
      .then(response => response.json())
      .then(apiData => 
        
        { console.log(apiData.item)
          setData(apiData.item)
        })
      .catch(error =>  console.error('error fetching data:', error));
  }, [])

  return (
    <div className='App'>

      <header className='App-header'>
        <h1>runescape ge</h1>

        <img src={data.icon_large} />
        <h2>{data.name}</h2>
        <p>{data.description}</p>
        <h3>Current Price: {data.current.price}</h3>
        <p>
          Price Drop Today: {data.today.price} {data.today.trend}
          Price Drop 30 days: {data.day30.change}{data.day30.trend}
          Price Drop 90 days: {data.day90.change}{data.day90.trend}
          Price Drop 180 days: {data.day180.change}{data.day180.trend}

        </p>
        <h3>Type of Item: <img src={data.typeIcon}/> {data.type}</h3>
        <h4>members item?: {data.members}</h4>

      </header>
    </div>
  )
}
 
export default App