/*
 * React Hooks Overview
 *
 * 1. useState
 * - Manages state in functional components
 * - Returns state value and update function
 */
const UseStateExample = () => {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
};

/*
 * 2. useEffect
 * - Handles side effects (data fetching, subscriptions, etc.)
 * - Runs after render, can clean up with return function
 */
const UseEffectExample = () => {
  const [data, setData] = useState(null);
  useEffect(() => {
    fetch("https://api.example.com")
      .then((res) => res.json())
      .then(setData);
    return () => console.log("Cleanup");
  }, []); // Empty array means run once on mount
};

/*
 * 3. useContext
 * - Accesses context values
 * - Avoids prop drilling
 */
const ThemeContext = createContext("light");
const UseContextExample = () => {
  const theme = useContext(ThemeContext);
  return <div>Current theme: {theme}</div>;
};

/*
 * 4. useReducer
 * - Manages complex state logic
 * - Alternative to useState with reducer pattern
 */
const reducer = (state, action) => {
  switch (action.type) {
    case "increment":
      return state + 1;
    default:
      return state;
  }
};
const UseReducerExample = () => {
  const [state, dispatch] = useReducer(reducer, 0);
  return (
    <button onClick={() => dispatch({ type: "increment" })}>{state}</button>
  );
};

/*
 * 5. useCallback
 * - Memoizes callback functions
 * - Prevents unnecessary re-renders
 */
const UseCallbackExample = () => {
  const [count, setCount] = useState(0);
  const increment = useCallback(() => setCount((c) => c + 1), []);
  return <button onClick={increment}>{count}</button>;
};

/*
 * 6. useMemo
 * - Memoizes expensive computations
 * - Only recomputes when dependencies change
 */
const UseMemoExample = () => {
  const [num, setNum] = useState(1);
  const expensiveCalc = useMemo(() => num * 100, [num]);
  return <div>{expensiveCalc}</div>;
};

/*
 * 7. useRef
 * - Creates mutable reference that persists across renders
 * - Useful for DOM access or storing previous values
 */
const UseRefExample = () => {
  const inputRef = useRef(null);
  const focusInput = () => inputRef.current.focus();
  return <input ref={inputRef} />;
};

/*
 * 8. useImperativeHandle
 * - Customizes instance value exposed to parent components
 * - Used with forwardRef
 */
const UseImperativeHandleExample = forwardRef((props, ref) => {
  const inputRef = useRef();
  useImperativeHandle(ref, () => ({
    focus: () => inputRef.current.focus(),
  }));
  return <input ref={inputRef} />;
});

/*
 * 9. useLayoutEffect
 * - Like useEffect, but runs synchronously after DOM mutations
 * - Useful for measurements
 */
const UseLayoutEffectExample = () => {
  const [width, setWidth] = useState(0);
  const divRef = useRef();
  useLayoutEffect(() => {
    setWidth(divRef.current.offsetWidth);
  }, []);
  return <div ref={divRef}>Width: {width}</div>;
};

/*
 * 10. useDebugValue
 * - Displays custom label in React DevTools
 * - Helps debug custom hooks
 */
const useCustomHook = () => {
  const [state, setState] = useState(0);
  useDebugValue(state > 0 ? "Positive" : "Zero or Negative");
  return state;
};
