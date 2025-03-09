const Table = ({ data }) => (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Price</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item) => (
          <tr key={item.id}>
            <td>{item.id}</td>
            <td>{item.price}</td>
            <td>{new Date(item.timestamp).toLocaleString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
  
  export default Table;
  