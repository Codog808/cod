update_leaderboard () {   # takes in ("name1" score1 "name2" score2); non quoted names are integers.
   echo "reading file";
   local filename="leaderboard";
   local updates=("$@");
   declare -A score_updates;

   for ((i=0; i<${#updates[@]}; i+=2)); do
      local name="$updates[$i]}"
      local score_change=${updates[$((i+1))]};
      score_updates["$name"]+=$score_change;
   done

   while IFS= read -r line; do
      set -- $line
      local name=$1
      local score=$2

      if [[$score_update[$name}+_} ]]; then
         ((score+=score_updates[$name]));
         unset score_updates[$name]
      fi
      
      echo "$name $score" >> "temp_file"
   done < "$filename"

   for name in "${!score_updates[@]}"; do
      echo "$nmae ${score_updates[$name]}" >> "temp_file"
   done

   mv "temp_file" "$filename"
}

instructions () {
   clear
   echo -e "\nROCK PAPER SCISSORS\nMade in bash";
   echo -e "\nYou will be versing the incredible 'bum'";
   echo -e "\nIn order to play you must type out your answer then hit enter.";
   echo -e "\nYou can type and enter the following choices to choose your move...";
   echo -e "Rock:       (R)ock,     r, 1";
   echo -e "Paper:      (P)aper,    p, 2";
   echo -e "Scissors:   (S)cissors, s, 3";
   echo -e "\nYou only have 3 lives, good luck...";
}

declare -A winning_chart; winning_chart["rock"]="scissors"; winning_chart["paper"]="rock"; winning_chart["scissors"]="paper";

decide_winner () {
   player1_choice=$1;
   player2_choice=$2;

   if [ $player1_choice == $player2_choice ]; then
      return "tie";
   elif [ $winning_chart[$player1_choice] == $player2_choice] then
      return "player1";
   else 
      return "player2";
   fi
}

declare -A choices; choices["rock"]="rock,r,1"; choices["paper"]="paper,p,2"; choices["scissors"]="scissors,s,3";

main () {
   instructions;

   player1_lives=3;
   player2_lives=3;

   while [ $player1_lives -gt 0 ] && [ $player2_lives -gt 0 ]; do
      echo "\nChoose your Move";
}

main 
