import { createContext, useState, useEffect } from 'react';
export const UserContext = createContext(null);

export function UserContextProvider({children}){
    //State to store table Column name
    const [tableRows, setTableRows] = useState([]);

    //State to store the values
    const [values, setValues] = useState([]);

    const [filetype,setFileType] = useState([]);
    const [File,setFile] = useState(null)
    const [name, setName] = useState("untitled flow");
    useEffect(
        ()=>{
          console.log("tablerows ",tableRows)
          setTableRows(tableRows)
        },[tableRows]
      )
    const value={
      name,
      setName,
        tableRows,
        setTableRows,
        values,
         setValues,
         filetype,
         setFileType,
         File,
         setFile
    }
     
    return(
        <UserContext.Provider value={value}>
            {children}
        </UserContext.Provider>
    )
}


  
     

