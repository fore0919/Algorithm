const solution = (n, lost, reserve) => {
    let Lost = lost.filter(a => !reserve.includes(a)); 
    let Reserve = reserve.filter(a => !lost.includes(a)); 
    return n - Lost.filter(lostStudent => {
        let extra = Reserve.find(reserveStudent => Math.abs(reserveStudent - lostStudent) <= 1);
      	if(!extra) return true;
      	Reserve = Reserve.filter(reserveStudent => reserveStudent !== extra);
    }).length;
}