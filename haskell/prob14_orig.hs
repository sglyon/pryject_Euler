collatz :: Int -> Int -> Int
collatz c 1 = c
collatz c k
    | even k    = collatz (c+1) (k `div` 2)
    | otherwise = collatz (c+1) (3*k + 1)

main = do
    print $ maximum (map (\i -> (collatz 1 i, i)) [1..1000000])
